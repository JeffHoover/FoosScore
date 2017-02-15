import sys, signal
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import AlphaNum4

IR_DETECT = 8
RESET_BUTTON = 36
score_a = 0
score_b = 0

def handle_ctrl_c(signal, frame):
    write_score("    ")
    sys.exit(130) # 130 is standard exit code for ctrl-c

def write_score(str):
    display.print_str(str)
    display.write_display()

def setup_LEDs():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(IR_DETECT, GPIO.IN)

def reset_game():
    global score_a
    global score_b
    score_a = 0
    score_b = 0
    write_score(" 0 0")
    time.sleep(0.4)


# BEGIN MAIN

display = AlphaNum4.AlphaNum4()
display.begin()
setup_LEDs()

signal.signal(signal.SIGINT, handle_ctrl_c)
GPIO.setup(RESET_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

reset_game()

while (1):
    if GPIO.input(RESET_BUTTON):
        reset_game()

    if not GPIO.input(IR_DETECT):
      score_a += 1
          
      if score_a > 7:
         scores = "WN 0"
      else:
          scores = " " + str(score_a) + " 0"

      display.print_str(scores)
      display.write_display()
      time.sleep(0.4)

