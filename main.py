# Import necessary libraries
import RPi.GPIO as GPIO
from RPLCD import CharLCD

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Define the LCD pin connections (adjust these based on your wiring)
lcd = CharLCD(cols=20, rows=4, pin_rs=25, pin_e=24, pins_data=[23, 17, 27, 22], numbering_mode=GPIO.BCM)

# Clear the LCD screen
lcd.clear()

# Display text on the LCD
lcd.write_string("Hello, World!")
lcd.cursor_pos = (1, 0)  # Set the cursor to the second line
lcd.write_string("20x4 LCD Test")
lcd.cursor_pos = (2, 0)  # Set the cursor to the third line
lcd.write_string("Raspberry Pi")
lcd.cursor_pos = (3, 0)  # Set the cursor to the fourth line
lcd.write_string("LCD Example")

# Wait for a few seconds
import time
time.sleep(5)

# Clear the LCD screen and cleanup GPIO
lcd.clear()
GPIO.cleanup()
