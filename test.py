import sys, signal
import os, subprocess
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import AlphaNum4

RESET_BUTTON = 36
BALL1 = 37
BALL2 = 15
SCORE_TO_WIN = 7

score_a = 0
score_b = 0
winner = 0
scores = "     "

def handle_ctrl_c(signal, frame):
    write_score("    ")
    sys.exit(130) # 130 is standard exit code for ctrl-c

def write_score(str):
    display.print_str(str)
    display.write_display()
#    print(str, flush=True)

def setup_LEDs():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(BALL1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BALL2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def reset_game():
    global score_a
    global score_b
    score_a = 0
    score_b = 0
    write_score(" 0 0")
    time.sleep(0.8)

def is_winning_score(score):
    return score >= SCORE_TO_WIN

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
        winner = 0

    if winner == 0:
       if GPIO.input(BALL1):
         score_a += 1
       if GPIO.input(BALL2):
         score_b += 1
          
    scores = " " + str(score_a) + " " + str(score_b)

    if is_winning_score(score_a):
       scores = "WN " + str(score_b)
       winner = 1

    if is_winning_score(score_b):
       scores = str(score_a) +" WN"
       winner = 2

    write_score(scores)
    time.sleep(1.4)

