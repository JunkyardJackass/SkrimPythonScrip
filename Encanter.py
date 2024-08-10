#!/usr/bin/env python3

import pyautogui
import time
import threading
import keyboard

#Why threading? It wont run correct without, or at least it wont fn stop...
#Update, it wont stop still.
stop_event = threading.Event()

def K(key):
    if key in ('e', 'w', 'a', 's', 'd', 'r', 'y'):
        pyautogui.keyDown(key)
        time.sleep(0.05)
        pyautogui.keyUp(key)
        time.sleep(0.1)
        
        #JFC STOP NOW GOD DAMN IT.
        if stop_event.is_set():
            return

def perform_sequence():

    #You can do with the sequence what the hell you want. IDC...
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'a', 'w', 'd', 'e', 'r', 'y']
    while not stop_event.is_set():
        for key in sequence:
            K(key)
            if stop_event.is_set():
                break
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

monitor_stop_key()

sequence_thread.join()
print("Sequence stopped.")

