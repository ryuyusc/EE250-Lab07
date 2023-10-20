import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)
#Following commands control the state of the output
#GPIO.output(pin, GPIO.HIGH)
#GPIO.output(pin, GPIO.LOW)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# get reading from adc 
# mcp.read_adc(adc_channel)

# starts with LED off
GPIO.output(11, GPIO.LOW)

while True: 
  # blinks LED 5 times
  for i in range(0, 5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5) 
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
  
  #reads light sensor
  for i in range(0, 50):
    light = mcp.read_adc(0)
    lightValue = int(light)
    if (lightValue > 150):
      print("bright")
    else:
      print("dark")
    print(light)
    time.sleep(0.1)
  
  #blinks LED 4 times
  for i in range(0, 4):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.2)

  # reads sound sensor
  for i in range(0, 50):
    sound = mcp.read_adc(1)
    soundValue = int(sound)
    if (soundValue > 820):
      GPIO.output(11, GPIO.HIGH)
    print(sound)
    time.sleep(0.1)
    GPIO.output(11, GPIO.LOW)


  
 