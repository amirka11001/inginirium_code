import keyboard
import pyautogui

x = 0
z = 0
y = 0

keyboard.press('windows')
keyboard.release('windows')

keyboard.press('down')
keyboard.release('down')
i_1 = 1
if i_1 == 1:
    for i in range(10):
        pyautogui.moveTo(1275, 955, duration=0.10)
        x = 1

    if x == 1:
        pyautogui.click()
        pyautogui.moveTo(1275, 870, duration=0.10)
        z = 1

    if z == 1:
        pyautogui.moveTo(1275, 870, duration=0.10)
        y = 1

    if y == 1:
        for i in range(0, 2, 1):
            pyautogui.click()