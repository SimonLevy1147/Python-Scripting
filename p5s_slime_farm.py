import pyautogui
import pydirectinput

pyautogui.hotkey('alt', 'tab')
pyautogui.sleep(1)

while (True):
    pydirectinput.press('space')
    pyautogui.sleep(1.5)
    pydirectinput.press('space')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(2)
    pydirectinput.press('2')
    pyautogui.sleep(0.5)
    pydirectinput.press('up')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(3)