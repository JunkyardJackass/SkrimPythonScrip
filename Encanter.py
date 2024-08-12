#!/usr/bin/env python3

import pyautogui
import time
import threading
import keyboard

# Read the README. Have a day.

stop_event = threading.Event()
running_event = threading.Event()

def K(key):
    if key in ('e', 'w', 'a', 's', 'd', 'r', 'y'):
        pyautogui.keyDown(key)
        time.sleep(0.05)
        pyautogui.keyUp(key)
        time.sleep(0.1)
        if stop_event.is_set():
            return

def Enchant():
    """ 
    # WEAPON Enchants, requires additional E key command, uncomment to activate. (Delete the quotations and use the 3 quotes on the other stack.)
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'e', 'a', 'w', 'd', 'e', 'r', 'y']
    """
    # Armour Enchants, requires only one E key command to pass, uncomment to activate. (Delete the quotations and use the 3 quotes on the other stack.)
    sequence = ['d', 'e', 'a', 's', 'd', 'e', 'a', 's', 'd', 'e', 'r', 'y',
                'e', 'a', 'w', 'd', 'e', 'a', 'w', 'd', 'e', 'r', 'y']

    while not stop_event.is_set():
        while running_event.is_set() and not stop_event.is_set():
            for key in sequence:
                if stop_event.is_set() or not running_event.is_set():
                    break
                K(key)
            time.sleep(0.1)

def E_Spam():
    while not stop_event.is_set():
        if keyboard.is_pressed('f3'):
            while keyboard.is_pressed('f3') and not stop_event.is_set():
                pyautogui.press('e')
                time.sleep(0.025)

def Enchant_Toggle_Key():
    while not stop_event.is_set():
        if keyboard.is_pressed('u'):
            if running_event.is_set():
                running_event.clear()  # Stop the Enchant sequence
            else:
                running_event.set()  # Start the Enchant sequence
            time.sleep(0.3)  #Stops a tism. Don't remove.

def Enchant_EBRAKE(): #Why? Because it wont stop sometimes if this isnt there.
    #Why not rely on the toggle key? Because sometimes it wont stop.
    while not stop_event.is_set():
        if keyboard.is_pressed('u'):
            stop_event.set()
            break

print("Starting in 5 seconds...")
time.sleep(5)
print("Started!")

sequence_thread = threading.Thread(target=Enchant)
sequence_thread.start()

toggle_thread = threading.Thread(target=Enchant_Toggle_Key)
toggle_thread.start()

stop_thread = threading.Thread(target=Enchant_EBRAKE)
stop_thread.start()

e_key_thread = threading.Thread(target=E_Spam)
e_key_thread.start()

sequence_thread.join()
toggle_thread.join()
stop_thread.join()
e_key_thread.join()

print("Sequence stopped.")
