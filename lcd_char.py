# Subscriber list, displayed on rotation on a character LCD
import Adafruit_CharLCD
import time

# Init LCD
lcd_rs = 16
lcd_en = 20
lcd_d4 = 6
lcd_d5 = 13
lcd_d6 = 19
lcd_d7 = 26
lcd_columns = 16
lcd_rows = 2
lcd_backlight = 4
lcd = Adafruit_CharLCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Load sub data
subs = []
with open('Subs.txt') as f:
	for line in f:
		partial_lines = line.split('|')
		new_partial = []
		for s in partial_lines:
			stripped = s.strip()
			new_partial.append(stripped)
		subs.append('\n'.join(new_partial))

#if __name__ == '__main__':
