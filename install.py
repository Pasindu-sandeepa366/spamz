print('cheking....')
import os
lis=[]
try:
    import time
except:
    lis.append('time')
try:
    import pynput
except:
    lis.append('pynput')
try:
    import pyautogui
except:
    lis.append('pyautogui')
try:
    import colorama
except:
    lis.append('colorama')
try:
    import os
except:
    lis.append('os')
try:
    import platform
except:
    lis.append('platform')
try:
    import clipboard
except:
    lis.append('clipbord')
print('installing modules')
for i in lis:
    os.system(f'pip install {i}')
