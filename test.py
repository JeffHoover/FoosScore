import sys, signal
import RPi.GPIO as GPIO
#from Adafruit_LED_Backpack import AlphaNum4

#RED = 7
#YELLOW = 3
#GREEN = 5
IR_DETECT = 8
IR_TRIG = 16

def handle_ctrl_c(signal, frame):
    extinguish_LEDs()
    sys.exit(130) # 130 is standard exit code for ctrl-c

def extinguish_LEDs():
    GPIO.output(IR_TRIG,1)
#    GPIO.output(YELLOW,0)
#    GPIO.output(GREEN,0)
#    GPIO.output(RED,0)

def setup_LEDs():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
#    GPIO.setup(RED, GPIO.OUT)
#    GPIO.setup(YELLOW, GPIO.OUT)
#    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(IR_DETECT, GPIO.IN)
    GPIO.setup(IR_TRIG, GPIO.OUT)

#display = AlphaNum4.AlphaNum4()
#display.begin()
setup_LEDs()
#GPIO.output(YELLOW,0)
#GPIO.output(GREEN,1)
#GPIO.output(RED,0)
GPIO.output(IR_TRIG,1)

#display.print_str("11 9")
#display.write_display()

signal.signal(signal.SIGINT, handle_ctrl_c)

while (1):
    if GPIO.input(IR_DETECT):
      print("HIGH")
      GPIO.output(IR_TRIG,1)
#      GPIO.output(GREEN,0)
#      GPIO.output(RED,1)
    else:
       print("LOW")
       GPIO.output(IR_TRIG,0)
#       GPIO.output(GREEN,1)
#       GPIO.output(RED,0)

