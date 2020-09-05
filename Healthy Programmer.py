# Healthy Programmer

"""
9am to 5pm
Water - water.mp3  (3.5 litres) - "Drank" - log
Eyes - eyes.mp3  - every 30 minutes - "EyDone" - log
Physical activity - physical.mp3  - every 45 minutes - "ExDone" - log
"""


import pygame

# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("song.mp3")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()

pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ").lower()

    if query == 'p':
        # Pausing the music
        pygame.mixer.music.pause()
    elif query == 'r':
        # Resuming the music
        pygame.mixer.music.unpause()
    elif query == 'e':
        # Stop the mixer
        pygame.mixer.music.stop()
        break
