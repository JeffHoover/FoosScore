import sys, signal
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import AlphaNum4

IR_DETECT = 8

def handle_ctrl_c(signal, frame):
    clear_score()
    sys.exit(130) # 130 is standard exit code for ctrl-c

def clear_score():
    display.print_str("    ")
    display.write_display()

def setup_LEDs():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(IR_DETECT, GPIO.IN)

display = AlphaNum4.AlphaNum4()
display.begin()
setup_LEDs()

display.print_str(" 0 0")
display.write_display()

score_a = 0
score_b = 0

signal.signal(signal.SIGINT, handle_ctrl_c)

reset_count = 0
scores = " 0 0"
while (1):
    if GPIO.input(IR_DETECT):
#      print("HIGH")
       b = 0;
    else:
#      print("LOW")
      score_a += 1
      if reset_count >= 10:
          reset_count = 0
          score_a = 0
          score_b = 0
          scores = " 0 0"
          
      if score_a > 7:
         print (str(reset_count))
         reset_count += 1
         scores = "WN 0"
      else:
          scores = " " + str(score_a) + " 0"

      display.print_str(scores)
      display.write_display()
      time.sleep(0.4)

