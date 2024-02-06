# INSTALLATION
# TOOLS > OPEN SYSTEM SHELL
# pip install pyautogui
# pip install keyboard
# Close Terminal, rerun script using F5 or the green check at the top
# Press F2 to start the script. Press F4 to stop the script at any time.
# After pressing F2, 
# If the script is sleeping or waiting, wait until it starts typing again to press F4 to stop it.
# The script will not stop if it is actively sleeping.
# Put your contents you wish to type into paste-here.txt

# The script will break at a percentage chance after typing a period (PERIOD_BREAK_CHANCE). The script will also automatically
# break randomly, this is called NORMAL_BREAK_CHANCE.

import time
import keyboard
import random
import pyautogui

# MINIMUM TIME IT'LL WAIT BEFORE PASTING THE NEXT CHARACTER
min_delay = 0.01

# MAX TIME IT'LL... (Change this value to lower if you want faster typing.
max_delay = 0.22

# MINIMUM TIME TO BREAK
min_break = 0.5

# MAXIMUM TIME TO BREAK
max_break = 1.5

# PERIOD BREAK PERCENTAGE CHANCE. 0.2 = 20%
PERIOD_BREAK_CHANCE = 0.2

# NORMAL BREAK PERCENTAGE CHANCE. 0.01 = 1%
NORMAL_BREAK_CHANCE = 0.01

# START KEY
START_KEY = 'F2'

# STOP KEY
STOP_KEY = 'F4'

# Get the paragraph from user input
def getText(filename):
    contents = []
    try:
        with open(filename, "r") as f:
            for line in f:
                contents.append(line)
            return contents
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def simulate_typing(min_delay, max_delay, min_break, max_break):
    input = getText('paste-here.txt')
    
    for text in input:
        for char in text:
            if keyboard.is_pressed(STOP_KEY):
                time.sleep(0.25)
                pyautogui.alert("Typing Canceled!")
                return
            keyboard.write(char)
            time.sleep(random.uniform(min_delay, max_delay))
            
            if char == ".":
                if random.random() < PERIOD_BREAK_CHANCE: # 40% chance of breaking after a period
                    break_duration = random.uniform(min_break, max_break)
                    time.sleep(break_duration * 1.25)
                
            # Taking a random break
            if random.random() < NORMAL_BREAK_CHANCE:  # 1% chance of taking a break
                break_duration = random.uniform(min_break, max_break)
                time.sleep(break_duration)
    
    pyautogui.alert("Finished Typing!")

            #pyautogui.press("space")  # Add space between words

def wait_for_start():
    while True:
        if keyboard.is_pressed(START_KEY):
            break
        time.sleep(0.1)
    pyautogui.alert("You've got 5 seconds to select the screen you want to start typing on. \nPress OK")


# Wait for F2 key press to start
wait_for_start()

# Wait for a brief moment to allow for box selection
time.sleep(5)

# Type the paragraph with randomized delays, breaks, and cancellation
simulate_typing(min_delay, max_delay, min_break, max_break)