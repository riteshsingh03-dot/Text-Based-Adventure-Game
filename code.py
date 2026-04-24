import os
import random
import msvcrt
import time

def welcome():
    os.system("cls")
    print("Welcome",end=" ")
    time.sleep(0.4)
    print("to",end=" ")
    time.sleep(0.4)
    print("the",end=" ")
    time.sleep(0.4)
    print("text-based",end=" ")
    time.sleep(0.4)
    print("adventure",end=" ")
    time.sleep(0.4)
    print("game",end=" ")
    time.sleep(0.4)
    os.system("cls")
    print("Starting",end="")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.2)
    return

def about():
    os.system("cls")
    print("Hello\n")
    time.sleep(0.55)
    print("This is a text based adventure game.")
    time.sleep(0.65)
    print("Hope you like it.")
    time.sleep(0.25)
    print("^_^")
    print("\n\nPress any key to go back.")
    msvcrt.getch()
    return

def end():
    os.system("cls")
    print("T",end="")
    time.sleep(0.2)
    print("H",end="")
    time.sleep(0.2)
    print("A",end="")
    time.sleep(0.2)
    print("N",end="")
    time.sleep(0.2)
    print("K",end=" ")
    time.sleep(0.2)
    print("Y",end="")
    time.sleep(0.2)
    print("O",end="")
    time.sleep(0.2)
    print("U",end=" ")
    time.sleep(0.2)
    print("^_^",end="")
    time.sleep(1)
    exit()

