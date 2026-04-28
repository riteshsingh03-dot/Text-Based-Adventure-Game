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

def long():
    time.sleep(1.45)
def suspense():
    time.sleep(2)
def quick():
    time.sleep(0.25)
def narr():
    time.sleep(1.20)
def notice():
    time.sleep(0.85)

def dots():
    time.sleep(0.35)
    print(".",end="")
    time.sleep(0.35)
    print(".",end="")
    time.sleep(0.35)
    print(".",end="")
    time.sleep(0.35)
    print(".",end="")
    time.sleep(0.35)

def scene1a():
    os.system("cls")

def scene1b():
    os.system("cls")

def scene1c():
    os.system("cls")

def scene1():
    os.system("cls")
    print("darkness",end="")
    dots()
    os.system("cls")
    time.sleep(0.85)
    print("THUD")
    long()
    print("You fall from your bed...")
    narr()
    print("You wake up and realise something",end=" ")
    narr()
    print("\"This is not my room.\"")
    long()
    print("You get up and notice something")
    notice()
    print("You are wearing a long brown coat")
    long()
    print("You check your pockets")
    long()
    dots()
    quick()
    print("You found a pen, a notebook, a badge.")
    long()
    print("Press e to interact with the badge")
    choice=msvcrt.getch().decode()
    if choice=="e":
        os.system("cls")
        time.sleep(0.45)
        print("You see the badge.")
        narr()
        print("The badge reads: Detective Mehul - Private Detective")
        long()
    else:
        print("You chose to ignore the badge.\n")
        long()
    
    print("\"What is this happening...\"\n")
    narr()
    print("A strange voice suddenly  fills the room.\n")
    narr()
    print("[Getting normal, are you?]")
    long()
    print("\"What!!\"")
    suspense()
    dots()
    dots()
    suspense()
    print("\"Is this game lagging\"\n")
    quick()
    print("[Absolutely Not!]")
    long()
    print("[Come on, It was just a dramatical pause.]")
    narr()
    print("[By the way, treat me with some respect]")
    narr()
    print("[I am your guardian angel.]\n")
    long()
    print("\"Am I dreaming..\"")
    quick()
    print("[Absolutely Not, You have been reincarnated as detective Mehul.]\n")
    long()
    print("\"Whatt!!, Why??")
    narr()
    print("[You really think you have a choice]")
    quick()
    print("\"Why don't I have one?\"")
    suspense()
    print("[Come on, Just Accept It.]\n\n")
    narr()
    print("Press any key to continue.")
    msvcrt.getch()
    print("Chose one Option: ")
    print("a) \"I really don't seem to have any choice.\"")
    print("b) \"How do you even think I am gonna agree to it...\"")
    print("c) \"As you say Sir...\"")
    time.sleep(0.25)
    ch1=msvcrt.getch().decode()
    while ch1!="a" and ch1!="b" and ch1!="c":
        print("Chose from the options(a,b,c).")
        time.sleep(0.15)
        ch1=msvcrt.getch().decode()
    
    if ch1=="a":
        scene1a()
    if ch1=="b":
        scene1b()
    if ch1=="c":
        scene1c()

scene1()

