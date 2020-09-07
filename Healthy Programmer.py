# Healthy Programmer

"""
9am to 5pm
Water - water.mp3 - every 40 minutes - (3.5 litres) - "Drank" - log
Eyes - eyes.mp3  - every 30 minutes - "EyDone" - log
Physical activity - physical.mp3  - every 45 minutes - "ExDone" - log
"""

from pygame import mixer
from datetime import datetime
from time import time


def playMusic(file, lopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input()
        if a.lower() == lopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("myLogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterSec = 40 * 60
    eyesSec = 30 * 60
    exerciseSec = 45 * 60

    while True:
        if (time() - init_water) > waterSec:
            print("Water drinking time. Enter 'water' to stop the alarm")
            playMusic("water.mp3", "water")
            init_water = time()
            log_now("Drank water at")

        if (time() - init_eyes) > eyesSec:
            print("Eye exercise time. Enter 'eye' to stop the alarm")
            playMusic("eye.mp3", "eye")
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if (time() - init_exercise) > exerciseSec:
            print("Physical activity time. Enter 'phy' to stop the alarm")
            playMusic("exercise.mp3", "phy")
            init_exercise = time()
            log_now("Physical activity done at")
