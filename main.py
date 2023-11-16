import win32api
import win32con

import time

import pyperclip

l = input("spam text: ")
b = int(input("times: "))
pause_user = float(input("pause between spam(in seconds): "))

if pause_user < 0:
    pause_user = 0


pyperclip.copy(l)


def press_ctrl_v():
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)

    win32api.keybd_event(ord('V'), 0, 0, 0)

    win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)

    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def press_enter():
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)

    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)


h = int(0)

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("start")

while h != b:
    press_enter()
    press_ctrl_v()
    press_enter()
    h += 1
    time.sleep(pause_user)

print("finished")