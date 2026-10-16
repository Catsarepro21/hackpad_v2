#include <Arduino.h>
#include <Wire.h>
#include <USB.h>
#include <USBHIDKeyboard.h>
#include <USBHIDConsumerControl.h>
#include <Adafruit_NeoPixel.h>

#define PIN_RGB_EN    1
#define PIN_RGB_DATA  2
#define PIN_SDA       5
#define PIN_SCL       6
#define PIN_ENC1_A    44
#define PIN_ENC1_B    7
#define PIN_ENC2_A    8
#define PIN_ENC2_B    9

#define MCP_ADDR      0x20
#define MCP_IODIR     0x00
#define MCP_IPOL      0x01
#define MCP_GPINTEN   0x02
#define MCP_DEFVAL    0x03
#define MCP_INTCON    0x04
#define MCP_IOCON     0x05
#define MCP_GPPU      0x06
#define MCP_INTF      0x07
#define MCP_INTCAP    0x08
#define MCP_GPIO      0x09
#define MCP_OLAT      0x0A

#define NUM_LEDS      12
#define MAX_BRIGHTNESS 64

USBHIDKeyboard Keyboard;
USBHIDConsumerControl ConsumerControl;
Adafruit_NeoPixel strip(NUM_LEDS, PIN_RGB_DATA, NEO_GRB + NEO_KHZ800);

const uint8_t keymap[2][3] = {
  {KEY_F13, KEY_F14, KEY_F15},
  {KEY_F16, KEY_F17, KEY_F18}
};

bool keyState[2][4] = {false};
bool lastReading[2][4] = {false};
unsigned long lastDebounceTime[2][4] = {0};
const unsigned long debounceDelay = 15;

volatile int32_t enc1Delta = 0;
volatile int32_t enc2Delta = 0;
uint8_t enc1State = 3;
uint8_t enc2State = 3;

const int8_t encTable[16] = {
   0, -1,  1,  0,
   1,  0,  0, -1,
  -1,  0,  0,  1,
   0,  1, -1,  0
};

void IRAM_ATTR isrEnc1() {
  uint8_t s = (digitalRead(PIN_ENC1_A) << 1) | digitalRead(PIN_ENC1_B);
  enc1State = ((enc1State << 2) | s) & 0x0F;
  enc1Delta += encTable[enc1State];
}

void IRAM_ATTR isrEnc2() {
  uint8_t s = (digitalRead(PIN_ENC2_A) << 1) | digitalRead(PIN_ENC2_B);
  enc2State = ((enc2State << 2) | s) & 0x0F;
  enc2Delta += encTable[enc2State];
}

void mcpWrite(uint8_t reg, uint8_t val) {
  Wire.beginTransmission(MCP_ADDR);
  Wire.write(reg);
  Wire.write(val);
  Wire.endTransmission();
}

uint8_t mcpRead(uint8_t reg) {
  Wire.beginTransmission(MCP_ADDR);
  Wire.write(reg);
  Wire.endTransmission(false);
  Wire.requestFrom((uint8_t)MCP_ADDR, (uint8_t)1);
  return Wire.available() ? Wire.read() : 0xFF;
}

void initMCP() {
  mcpWrite(MCP_OLAT, 0x00);
  mcpWrite(MCP_GPPU, 0x3C);
  mcpWrite(MCP_IODIR, 0x3F);
}

uint8_t scanRow(uint8_t row) {
  uint8_t iodir = (row == 0) ? 0x3E : 0x3D;
  mcpWrite(MCP_IODIR, iodir);
  delayMicroseconds(50);
  uint8_t gpio = mcpRead(MCP_GPIO);
  mcpWrite(MCP_IODIR, 0x3F);
  return (~gpio >> 2) & 0x0F;
}

void handleSwitchAction(uint8_t r, uint8_t c, bool pressed) {
  if (c < 3) {
    if (pressed) {
      Keyboard.press(keymap[r][c]);
    } else {
      Keyboard.release(keymap[r][c]);
    }
  } else {
    if (pressed) {
      if (r == 0) {
        ConsumerControl.press(CONSUMER_CONTROL_MUTE);
        ConsumerControl.release();
      } else {
        ConsumerControl.press(CONSUMER_CONTROL_PLAY_PAUSE);
        ConsumerControl.release();
      }
    }
  }
}

void setup() {
  pinMode(PIN_RGB_DATA, OUTPUT);
  digitalWrite(PIN_RGB_DATA, LOW);
  pinMode(PIN_RGB_EN, OUTPUT);
  digitalWrite(PIN_RGB_EN, LOW);

  pinMode(PIN_ENC1_A, INPUT_PULLUP);
  pinMode(PIN_ENC1_B, INPUT_PULLUP);
  pinMode(PIN_ENC2_A, INPUT_PULLUP);
  pinMode(PIN_ENC2_B, INPUT_PULLUP);

  enc1State = (digitalRead(PIN_ENC1_A) << 1) | digitalRead(PIN_ENC1_B);
  enc2State = (digitalRead(PIN_ENC2_A) << 1) | digitalRead(PIN_ENC2_B);

  attachInterrupt(digitalPinToInterrupt(PIN_ENC1_A), isrEnc1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_ENC1_B), isrEnc1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_ENC2_A), isrEnc2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_ENC2_B), isrEnc2, CHANGE);

  Wire.begin(PIN_SDA, PIN_SCL, 400000);
  initMCP();

  Keyboard.begin();
  ConsumerControl.begin();
  USB.begin();

  delay(20);
  digitalWrite(PIN_RGB_EN, HIGH);
  delay(10);

  strip.begin();
  strip.setBrightness(MAX_BRIGHTNESS);
  strip.clear();
  strip.show();
}

void loop() {
  unsigned long now = millis();

  for (uint8_t r = 0; r < 2; r++) {
    uint8_t cols = scanRow(r);
    for (uint8_t c = 0; c < 4; c++) {
      bool reading = (cols >> c) & 0x01;
      if (reading != lastReading[r][c]) {
        lastDebounceTime[r][c] = now;
      }
      if ((now - lastDebounceTime[r][c]) >= debounceDelay) {
        if (reading != keyState[r][c]) {
          keyState[r][c] = reading;
          handleSwitchAction(r, c, reading);
        }
      }
      lastReading[r][c] = reading;
    }
  }

  noInterrupts();
  int32_t d1 = enc1Delta;
  enc1Delta = d1 % 4;
  int32_t d2 = enc2Delta;
  enc2Delta = d2 % 4;
  interrupts();

  int32_t steps1 = d1 / 4;
  while (steps1 > 0) {
    ConsumerControl.press(CONSUMER_CONTROL_VOLUME_INCREMENT);
    ConsumerControl.release();
    steps1--;
  }
  while (steps1 < 0) {
    ConsumerControl.press(CONSUMER_CONTROL_VOLUME_DECREMENT);
    ConsumerControl.release();
    steps1++;
  }

  int32_t steps2 = d2 / 4;
  while (steps2 > 0) {
    Keyboard.write(KEY_PAGE_UP);
    steps2--;
  }
  while (steps2 < 0) {
    Keyboard.write(KEY_PAGE_DOWN);
    steps2++;
  }

  delay(1);
}
