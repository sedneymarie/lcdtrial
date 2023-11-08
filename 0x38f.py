import smbus2
import time

# Define I2C address
i2c_address = 0x3F

# Define I2C bus (you may need to adjust this for your specific Raspberry Pi model)
i2c_bus = 1

# Initialize I2C
bus = smbus2.SMBus(i2c_bus)

# LCD settings
lcd_width = 20  # 20 characters wide
lcd_lines = 4   # 4 lines

# LCD commands
lcd_clear = 0x01  # Clear display
lcd_home = 0x02   # Return to home
lcd_display_control = 0x08
lcd_display_on = 0x04
lcd_display_off = 0x00
lcd_cursor_on = 0x02
lcd_cursor_off = 0x00
lcd_blink_on = 0x01
lcd_blink_off = 0x00
lcd_set_cursor = 0x80

# Send command to the LCD
def lcd_command(command):
    bus.write_byte(i2c_address, command)
    time.sleep(0.005)  # 5ms delay

# Initialize the LCD
def lcd_init():
    lcd_command(0x33) # Initialize
    lcd_command(0x32) # Set to 4-bit mode
    lcd_command(0x06) # Set entry mode
    lcd_command(0x0C) # Turn on display
    lcd_command(0x28) # 2 lines, 5x8 matrix

# Clear the LCD
def lcd_clear_screen():
    lcd_command(lcd_clear)

# Set the LCD cursor position
def lcd_set_cursor(row, col):
    position = lcd_set_cursor + row * 0x40 + col
    lcd_command(position)

# Write text to the LCD
def lcd_write_text(text):
    for char in text:
        bus.write_byte(i2c_address, ord(char))
        time.sleep(0.002)

# Example usage
try:
    lcd_init()
    lcd_clear_screen()
    lcd_set_cursor(0, 0)
    lcd_write_text("Hello,")
    lcd_set_cursor(1, 0)
    lcd_write_text("Raspberry Pi!")
except KeyboardInterrupt:
    pass
finally:
    bus.close()
