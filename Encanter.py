#!/usr/bin/env python3

import pyautogui
import time
import threading
import keyboard

stop_event = threading.Event()

def K(key):
    if key in ('e', 'w', 'a', 's', 'd', 'r', 'y'):
        pyautogui.keyDown(key)
        time.sleep(0.05)
        pyautogui.keyUp(key)
        time.sleep(0.1)
        
        if stop_event.is_set():
            return

def perform_sequence():
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'a', 'w', 'd', 'e', 'r', 'y']
    while not stop_event.is_set():
        for key in sequence:
            K(key)
            if stop_event.is_set():
                break

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

sequence_thread.join()
stop_thread.join()

print("Sequence stopped.")
