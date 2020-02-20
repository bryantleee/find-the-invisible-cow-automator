import pyautogui
import pyperclip
import time

firefox_y_offset = 100

def copy_clipboard():
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def toggle_console():    
    pyautogui.hotkey('command', 'option', 'i')

def click_play():
    pyautogui.moveTo(100, 150)

def click_cow(coordinates):
    pyautogui.moveTo(coordinates[0], coordinates[1] + firefox_y_offset)
    pyautogui.click()

def get_coordinate(plane):
    pyautogui.typewrite('alert(window.app.children[1].__vue__._data.{})'.format(plane))
    pyautogui.hotkey('return')
    coordinate = copy_clipboard()
    pyautogui.hotkey('return')
    return int(coordinate.strip())

def get_coordinates():
    planes = ['x', 'y']
    coordinates = []
    for plane in planes:
        toggle_console()
        time.sleep(0.3)
        coordinates.append(get_coordinate(plane))
        toggle_console()
    return coordinates

def click_play_again():
    pyautogui.moveTo(457, 560)
    pyautogui.click()

if __name__ == '__main__':
    time.sleep(4)    
    while True:
        coordinates = get_coordinates()
        click_cow(coordinates)
        time.sleep(3)  
        click_play_again()
        time.sleep(1)  

