# KeyLogger
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/anish-agrahari/KeyLogger)

A simple Python-based keylogger designed for educational purposes. This script captures keyboard inputs and saves them with timestamps to a local file.

> **Disclaimer:** This tool is intended for educational and learning purposes only. Using this software on a computer without the owner's explicit permission is illegal. The author is not responsible for any misuse or damage caused by this program.

## Features

-   Captures both standard alphanumeric keys and special keys (e.g., `Shift`, `Enter`, `Esc`).
-   Adds a timestamp to every recorded keystroke for chronological tracking.
-   Saves all captured keystrokes to a log file named `keylog.txt`.
-   Provides a clean and safe way to stop the logger by pressing the `ESC` key.

## Prerequisites

This script requires Python 3 and the `pynput` library.

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/anish-agrahari/KeyLogger.git
    cd KeyLogger
    ```

2.  Install the necessary Python library:
    ```sh
    pip install pynput
    ```

## Usage

1.  Run the script from your terminal:
    ```sh
    python keylogger.py
    ```
    You will see the message `Starting keylogger...` in your console.

2.  The program will now run in the background, capturing all keyboard input.

3.  All keystrokes will be saved to the `keylog.txt` file in the same directory.

4.  To stop the keylogger, simply press the **`ESC`** key. A confirmation message `Keylogger stopped successfully.` will appear in the console.

## Log File Example

The output in `keylog.txt` will be formatted as follows, with each line containing a timestamp and the key that was pressed.

```
Keylogger started at 2026-04-08 21:35:04
[2026-04-08 21:35:09] Key.enter
[2026-04-08 21:35:10] Key.shift
[2026-04-08 21:35:10] H
[2026-04-08 21:35:11] e
[2026-04-08 21:35:12] l
[2026-04-08 21:35:12] l
[2026-04-08 21:35:12] o
[2026-04-08 21:35:12] Key.space
[2026-04-08 21:35:13] Key.shift
[2026-04-08 21:35:13] W
[2026-04-08 21:35:13] o
[2026-04-08 21:35:14] r
[2026-04-08 21:35:14] l
[2026-04-08 21:35:14] d
[2026-04-08 21:35:23] Key.esc
