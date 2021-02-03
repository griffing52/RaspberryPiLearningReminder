import duolingo
from time import time, sleep
from datetime import datetime

from playsound import playsound

lingo  = duolingo.Duolingo('GriffinG52', 'check223') # TODO add password

goal = 30
# xp = 0
xp = lingo.get_daily_xp_progress()["xp_today"]
print("checking")
print(datetime.now().hour)
if (xp >= goal):
    print("You did it!")
    playsound("goodJob.mp3")
    playsound("clapping.mp3")
elif (xp > 0):
    print("You are getting closer; keep working")
    playsound("encouragement.mp3")
elif (datetime.now().hour >= 19):
    playsound("imperial.mp3")
else:
    playsound("threat.mp3")