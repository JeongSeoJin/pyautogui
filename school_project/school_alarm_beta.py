import pyautogui

path = "C:\\Users\\정성환\\Desktop\\7.png"
i = pyautogui.locateOnScreen(path)
print(i)
# c = pyautogui.center(i)
# pyautogui.doubleClick(c)