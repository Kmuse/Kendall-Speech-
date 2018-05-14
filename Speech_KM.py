import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your favorite music artist?")

answer = pg.prompt("Enter your favorite artist below.")

if answer == "Drake":
    speak.Speak("same.")
elif answer == "Chance the Rapper":
    speak.Speak("He is great!")


speak.Speak("whats your favorite animal?")

animal = pg.prompt("Enter your favorite animal below.")

speak.Speak("Ok, searching youtube for funny" + animal + "videos.")

wb.open("https://www.youtube.com/results?search_query=" + "funny" + animal + "videos")
