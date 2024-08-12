#!/usr/bin/env python3

import pyautogui
import time
import threading
import keyboard

# Read the README. Have a day.

stop_event = threading.Event()
f3_event = threading.Event()

def K(key):
    if key in ('e', 'w', 'a', 's', 'd', 'r', 'y'):
        pyautogui.keyDown(key)
        time.sleep(0.05)
        pyautogui.keyUp(key)
        time.sleep(0.1)
        if stop_event.is_set():
            return

def perform_sequence():
    """ # WEAPON enchants, requires additional E key command, uncomment to activate.
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'e', 'a', 'w', 'd', 'e', 'r', 'y']
    """
    # Armour enchants, requires only one E key command to pass, uncomment to activate.
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'a', 'w', 'd', 'e', 'r', 'y']

    while not stop_event.is_set():
        for key in sequence:
            if stop_event.is_set():
                break
            K(key)

# This SHOULD, and I cant stress how little I KNOW it will work, Spam E on pressing F3.
# I PERSONALLY configured my mouse to have the F3 key programmed to it.
# None of this portion is tested and I stole it from ChatGPT but don't have time to test.
def simulate_e_key():
    while not stop_event.is_set():
        if keyboard.is_pressed('f3'):
            f3_event.set()
            while keyboard.is_pressed('f3') and not stop_event.is_set():
                pyautogui.press('e')
                time.sleep(0.025)
            f3_event.clear()

def monitor_stop_key():
    while not stop_event.is_set():
        if keyboard.is_pressed('u'):
            stop_event.set()
            break

print("Starting in 5 seconds...")
time.sleep(5)
print("Started!")

sequence_thread = threading.Thread(target=perform_sequence)
sequence_thread.start()

stop_thread = threading.Thread(target=monitor_stop_key)
stop_thread.start()

e_key_thread = threading.Thread(target=simulate_e_key)
e_key_thread.start()

monitor_stop_key()

sequence_thread.join()
stop_thread.join()
e_key_thread.join()

print("Sequence stopped.")
