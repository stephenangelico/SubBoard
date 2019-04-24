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
		subs.append(new_partial)

# Rotation of displayed sub
def rotate_sub():
	while True:
		for sub in subs:
			lcd.clear()
			#TODO: Horizontally scroll long names?
			first_line = sub[0]
			try:
				second_line = sub[1]
			except IndexError:
				second_line = "" # There is no second line
			lcd.message(first_line + "\n" + second_line)
			if len(first_line) > lcd_columns or len(second_line) > lcd_columns:
				first_line += " "
				second_line += " "
				for frame in range(max(len(first_line), len(second_line))):
					if len(first_line) > lcd_columns:
						first_line = first_line[1:] + first_line[0]
					if len(second_line) > lcd_columns:
						second_line = second_line[1:] + second_line[0]
					lcd.clear()
					lcd.message(first_line + "\n" + second_line)
					time.sleep(0.1)
			time.sleep(5)

if __name__ == '__main__':
	try:
		rotate_sub()
	finally:
		lcd.clear()
