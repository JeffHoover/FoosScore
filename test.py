import sys, signal
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import AlphaNum4

IR_DETECT = 8
IR_TRIG = 16

def handle_ctrl_c(signal, frame):
    extinguish_LEDs()
    clear_score()
    sys.exit(130) # 130 is standard exit code for ctrl-c

def clear_score():
    display.print_str("    ")
    display.write_display()

def extinguish_LEDs():
    GPIO.output(IR_TRIG,1)

def setup_LEDs():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(IR_DETECT, GPIO.IN)
    GPIO.setup(IR_TRIG, GPIO.OUT)

display = AlphaNum4.AlphaNum4()
display.begin()
setup_LEDs()
GPIO.output(IR_TRIG,1) # IR_TRIG will light on detection. LATER: need to hardwire an always on and test for beam break

display.print_str(" 0 0")
display.write_display()

score_a = 0
score_b = 0

signal.signal(signal.SIGINT, handle_ctrl_c)

scores = " 0 0"
while (1):
    if GPIO.input(IR_DETECT):
#      print("HIGH")
      GPIO.output(IR_TRIG,1)
    else:
#      print("LOW")
      score_a += 1
      if score_a > 99:
         score_a = 0
      if score_a < 10:
          scores = " 0 " + str(score_a)
      else:
          scores = " 0" + str(score_a)
      display.print_str(scores)
      display.write_display()
      time.sleep(0.4)
      GPIO.output(IR_TRIG,0)

