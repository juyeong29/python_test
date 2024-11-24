# include the Adafruit NeoPixel library code:
# https://github.com/adafruit/Adafruit_NeoPixel
from Adafruit_NeoPixel import *
import time

# specify the number of pixels and pin where the strip is connected to:
strip = 네오픽셀(12, 4)

# set the pixel color using HSB values:
strip.setPixelColor(0, 150, 0, 255)
strip.show()
time.sleep(5)

# create a function that changes the brightness based on the value returned by the light sensor:
def changeBrightne():
  brightne = analogRead(A0)
  if brightne > 500:
    brightne = map(brightne, 0, 1023, 0, 255)
  else:
    brightne = map(brightne, 0, 1023, 0, 100)
  return brightne

while True:
  # read the value from the light sensor every second:
  brightne = change Brightness()
  for i in range(strip.numPixels()):
    # set each pixel's RGB value according to the brightness level:
    strip.setPixelColor(i, brightne, brightne, brightne)
  strip.show()
  time.sleep(1)
