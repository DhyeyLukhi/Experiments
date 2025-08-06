import keyboard
import time

def recordKeys():
    while True:
        keys = keyboard.read_key()
        event = keyboard.is_pressed(hotkey=keys)
        if event:
            print(f"Yes Checked {keys}")
        

        
       

if __name__ == "__main__":
    recordKeys()