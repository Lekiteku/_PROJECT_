from pynput.mouse import Button, Controller4
import cv2
import face_recognition
import time
import random
import pyautogui
time.sleep(2)
x = 370
y = 500


#sucesss coordinates
x1 = 470
y1 = 150

# pyautogui.click(288, 458) #coodinate for butooon
color = pyautogui.pixel(x,y)
r = color[0]
g = color[1]
b = color[2]
pyautogui.moveTo(x, y)
count = 0
while True:
    color = pyautogui.pixel(x,y)
   # color1 = pyautogui.pixel(x1,y1)
    
    r = color[0]
    g = color[1]
    b = color[2]
    a,b = pyautogui.position()
    print(a)
    print(b)
    # r1 = color1[0]
    # g1 = color1[1]
    # b1 = color1[2]
    # add= random.randint(0, 10)
    # print(f"THIS IS ADD {add}")

        
    # while  g > 160 and r < 60:
    #     print("green click once")
    #     if g < 15:#and g > 160 and b < 20:
    #         print("r ")
    #         break

    
    #     #pyautogui.click(x, y)

    # while  g < 15:
    #     print("red here we go ")
    #     if r > 200 and g > 100 and b < 20:
    #         print("yellow states ")
    #         break

    # while r > 200 and g > 100 and b < 20:
    #     # pyautogui.click(x, y)
    #     if r > 160 and g < 60:
    #         print("yellow states ")
    #         break
    #     print("yellow")
    #     count = count + add  
        

    # else:
    #     print("wtf")

    # # if g1 > 160 and r1 < 60:
    # #     # pyautogui.click(x, y)
    # #     pyautogui.moveTo(x1, y1,2)
    # #     print("success")

    
    # print(x) 
    # print(color)    # break
    # a,b = pyautogui.position()
    # print(a)
    # print(b)
    # print(f"THIS IS count{count}")












# if r in range(50,60) and g in range(200,205) and b in range(15,20) :
#     print("yes")
# while True:
#     color = pyautogui.pixel(x,y)
#     print(color)
#     print(x)
#     print(y)
#     x,y = pyautogui.position()

# print(x)