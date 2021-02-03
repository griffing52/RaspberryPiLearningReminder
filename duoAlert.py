#import duolingo
import pygame
from time import time, sleep
from datetime import datetime

# lingo  = duolingo.Duolingo('GriffinG52', '...') # TODO add password

goal = 50


pygame.mixer.init()

print("checking")
print(datetime.now().hour)
# xp = lingo.get_daily_xp_progress()["xp_today"]
xp = 0
if (xp >= goal):
    print("You did it!")
    pygame.mixer.music.load("goodJob.mp3")
    pygame.mixer.music.load("clapping.mp3")
elif (xp > 0):
    print("You are getting closer; keep working")
    pygame.mixer.music.load("encouragement.mp3")
elif (datetime.now().hour >= 19):
    pygame.mixer.music.load("imperial.mp3")
else:
    pygame.mixer.music.load("threat.mp3")

pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue