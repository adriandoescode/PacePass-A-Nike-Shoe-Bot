from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading
import os

#Tile 1 Position: X:  581 Y:  400 RGB: ( 77,  80, 115)
#Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
#Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

os.system("cls")

event = threading.Event()
print((r"""
██████╗  █████╗  ██████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║██║     █████╗  
██╔═══╝ ██╔══██║██║     ██╔══╝  
██║     ██║  ██║╚██████╗███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
"""),(r"""

                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
    /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
            """))



event.clear()
start = input("Welcome to Pace!\n Type y to start! \n: ")
if start == "y":
    event.set()
else:
    print("Please type y to contine!")
event.wait()
    

def main():
    print(datetime.datetime.now(),"Starting....")
    time.sleep(2)
    

    while keyboard.is_pressed('q') == False:
        event.clear()
        if pyautogui.pixel(804, 1012)[0] == 0:
            click(804, 1012)
            print(datetime.datetime.now(),"\u001b[32m. Found Product!")
            event.set()
            break
        else:
            print(datetime.datetime.now(),"\u001b[33m. Waiting For Sale........")
            
    event.wait()
    while keyboard.is_pressed('q') == False:
        event.clear()
        if pyautogui.locateOnScreen("realreserve.png", region=(600,200,700,600), grayscale=True, confidence=0.8): 
            pyautogui.click("realreserve.png")
            print(datetime.datetime.now(),"\u001b[32m. Found Reserve!")
            event.set()
            break
        else:
            print(datetime.datetime.now(),"\u001b[33m. Fully Booked...")
            
    event.wait()  
    while keyboard.is_pressed('q') == False:
        event.clear()
        if pyautogui.pixel(804,1012)[0] == 0:
            click(804, 1012)
            print(datetime.datetime.now(),"\u001b[32m. Reserving....")
            event.set()
            break
        else:
            print(datetime.datetime.now(),"\u001b[31m. Finding Reserve now.. ")
            
    event.wait()

    event.clear()
    restart = input("\u001b[37m. Conragulations!, Would you like to Restart?\n Type y to restart! \n: ")
    if restart == "y":
        main()
    else:
        exit()
main()



