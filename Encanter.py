#!/usr/bin/env python3

import pyautogui
import time
import threading
import keyboard

"""
In file ReadMe.(why? because im not explaining.)
    SET UP: SKYRIM ENCHANTING
    
    Enchanting weapons requires the user to hit E twice (to adjust the calibre of the enchant), 
        if you would like this function added, you need to swap the commented sections as needed.
    Swap the comments to activate and deactivate the set up as needed.

***ENCHANTING INSTRUCTIONS***
Open enchanting screen in game.
Empty non consumables from inventory that you don't want used for the process.
    The macro does not care about your items, Dump entire inventory except what is used for enchanting...    
Start the enchanter
Set up, but do not actually enchant anything. 
    Run the process but do not start it.
    Set WHAT enchant you want applied to the items by selecting it at least once, and then UNAPPLY the selection.
    (I cant prove it, but enchants which make better value for item SHOULD make your more XP)
    ENSURE no selections are made and hover over the ITEMS line.    
Launch the macro, this script, left click into the game again.
Process should auto burn any consumables for the process that are in your inventory.
Press U to shut the secquence down, or if thats not working because im a lunatic, close the program.

"""

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
