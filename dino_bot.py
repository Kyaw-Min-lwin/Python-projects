import pyautogui
import time

# import win32api, win32con
# import keyboard

# import random

# ls = ['hello', 'how are u', 'this is a spam', 'i m spamming', 'this is a bot']
# pyautogui.keyDown('shift') # Press the Shift key down and hold it.
# pyautogui.press(['left', 'left', 'left', 'left'], interval=3)
# pyautogui.hotkey('ctrl', 'space')
# pyautogui.dragTo(100, 100, duration=3)
# time.sleep(3)
# for i in range(20):
#     pyautogui.write(random.choice(ls), interval=0.05)
#     pyautogui.press('enter')
# pyautogui.press('up')
# time.sleep(3)
# pyautogui.scroll(50)
# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.5)
# pyautogui.alert('This displays some text with an OK button.')
# pyautogui.confirm('This displays text and has an OK and Cancel button.')
# a = pyautogui.prompt('This lets the user type in a string and press OK.')
# print(a)
# print(pyautogui.position())  # Point(x=466, y=262)
# time.sleep(7)
# print('started')
# count = 100
#

#

# import pyautogui as gui
# import keyboard
# import time
# import math
#
# # Screen Dimensions for screen of size 1920X1080
# top, left, width, height = 293, 0, 700, 465
#
# # helper variables to calculate time
# last = 0
# total_time = 0
#
# # the intervals where the bot will search for obstacles
# y_search_cactus, x_start, x_end = 263, 495, 515
# y_search_bird = 270  # for the birds
#
# time.sleep(4)

# print(pyautogui.locateCenterOnScreen('seven.png', confidence=0.5))

# while True:
#     try:
#         if pyautogui.pixelMatchesColor(530, 255, (83, 83, 83)):
#             pyautogui.press('up')
#             time.sleep(0.1)
#             pyautogui.press('down')
#             continue
#         if pyautogui.pixelMatchesColor(520, 238, (83, 83, 83)):
#             pyautogui.press('up')
#             continue
#     except:
#         pass
# print(pyautogui.position())

while True:
    a = pyautogui.locateCenterOnScreen('cactus.png', confidence=0.26, region=(520, 200, 120, 90))
    if a is not None:
        pyautogui.press('up')
        time.sleep(0.17)
        pyautogui.press('down')
# pyautogui.moveTo(625, 300)
# print(pyautogui.position())  # left =478, top=327
