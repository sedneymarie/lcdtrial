import RPi.GPIO as GPIO
from RPLCD import i2c
import time

# Define the I2C address (usually 0x27) and bus number (usually 1)
lcd = i2c.CharLCD('PCF8574', 0x27)

try:
    # Clear the LCD screen
    lcd.clear()

    # Display text on the LCD
    lcd.write_string("Hello, World!")
    time.sleep(2)

    # Clear the LCD screen
    lcd.clear()

    # Display more text
    lcd.write_string("LCD with Raspberry Pi")
    time.sleep(2)

finally:
    # Clean up and close the LCD
    lcd.close(clear=True)
