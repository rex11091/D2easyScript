import pythoncom
import pyHook
from sendKeysTest import PressKey, ReleaseKey
import pyautogui
import time
from PIL import ImageGrab
import numpy as np
import cv2

Q = 0x10
W = 0x11
E = 0x12
R = 0x13
D = 0x20
F = 0x21
C = 0x2E
TAB = 0x0F

def OnKeyboardEvent(event):
    print(event.Key)
    if event.Key == 'Subtract':
        print("here")
        print("event key: ", event.Key)
        # alacrity()
        poof()
    elif event.Key == 'Add':
        pyautogui.moveTo(1125, 968)
        pyautogui.dragTo(1125, 929, 0.1001, button='left')
    elif event.Key == 'Multiply':
        #demonstration
        alacrity()
        pressKeyboard(Q)
        pressKeyboard(Q)
        pressKeyboard(Q)
        pressKeyboard(R)
        time.sleep(0.1)

        # TODO: get to the center of hero with certain algorithm

        x, y = get_hero_loc()

        pyautogui.moveTo(x, y+40)                        # Note ************************
        pressKeyboard(D)                                 # This is some useless program
        pyautogui.click()                                # develop this just to play games
        # cv2.imshow('window', image)                    # Please make a rocket instead
    elif event.Key == 'Divide':                          # I just want to type something
        pressKeyboard(C)                                 # Your keyboard really nice to type
        x, y = get_hero_loc()
        pyautogui.moveTo(x, y+40)
        pyautogui.click()
        time.sleep(0.85)
        pressKeyboard(D)
        pyautogui.click()
    # elif event.Key == 'G':
        pressKeyboard(C)
        pyautogui.click()
        time.sleep(1.5)
        pressKeyboard(W)
        pyautogui.click()
    elif event.Key == 'Numpad3':
        x, y = get_hero_loc()
        # print(x, y)

    # return True to pass the event to other handlers
    return True

def get_hero_loc():
    # get the screen, filter out every color except red, and find contours
    printscreen = np.array(ImageGrab.grab())
    lower = np.array([170, 40, 0])
    upper = np.array([200, 60, 0])
    shape_mask = cv2.inRange(printscreen, lower, upper)
    image, contours, hierarchy = cv2.findContours(shape_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for i in contours:
    #     np.sort(i)
    previous_max = 0
    previous_min = 1080
    for element in contours:
        max_val = np.amax(element)
        min_val = np.amin(element)
        if max_val > previous_max:
            previous_max = max_val
        if min_val < previous_min:
            previous_min = min_val

    print(previous_max)
    print(previous_min)
    print("------------------")
    print(contours)

    # print(type(contours))
    # print((contours[0]))
    randPlace = contours[0][0]
    # print(randPlace.flat[0])
    # print(randPlace.flat[1])
    return randPlace.flat[0], randPlace.flat[1]

def processImg(image):
    # convert to gray
    original_image = image
    processedImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processedImg = cv2.Canny(processedImg, threshold1=200, threshold2=300)
    return processedImg

def alacrity():
    pressKeyboard(W)
    pressKeyboard(W)
    pressKeyboard(E)
    pressKeyboard(R)
    time.sleep(0.2)
    pressKeyboard(D)
    pressKeyboard(D)
    time.sleep(0.2)
    pressKeyboard(W)
    pressKeyboard(W)
    pressKeyboard(W)

def poof():
    pressKeyboard(TAB)
    pressKeyboard(W)
    pressKeyboard(TAB)
    pressKeyboard(W)
    pressKeyboard(TAB)
    pressKeyboard(W)

def earthSpiritStun():
    pressKeyboard(D)
    pressKeyboard(D)
    PressKey(Q)

def pressKeyboard(vkCode):
    PressKey(vkCode)
    ReleaseKey(vkCode)

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse event
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
