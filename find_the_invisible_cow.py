import pyautogui
import pyperclip
import time
import re

firefox_y_offset = 100

def copy_clipboard():
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def toggle_console():
    pyautogui.hotkey('command', 'option', 'i')

def click_cow(coordinates):
    pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]) + firefox_y_offset)
    pyautogui.click()

def get_coordinates():
    toggle_console()
    time.sleep(0.08)
    pyperclip.copy('alert(window.app.children[1].__vue__._data.x + ", " + window.app.children[1].__vue__._data.y)')
    pyautogui.hotkey('command', 'v')
    pyautogui.hotkey('return')
    time.sleep(.01)
    coordinates = re.findall('(\d+), (\d+)', copy_clipboard())
    pyautogui.hotkey('return')
    toggle_console()
    return coordinates[0]

def click_play_again():
    pyautogui.moveTo(457, 560)
    pyautogui.click()

if __name__ == '__main__':
    time.sleep(2)
    while True:
        coordinates = get_coordinates()
        click_cow(coordinates)
        time.sleep(2.25)
        click_play_again()
        time.sleep(0.05)

