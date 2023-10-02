import pyautogui
from time import sleep

n=int(input())
sleep(5)

i=0
j=0
while i<n:
    while j<=i:
        pyautogui.write('#')
        j+=1
    pyautogui.write('\n')

    i+=1
    j=0

