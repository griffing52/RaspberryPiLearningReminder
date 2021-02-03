# RaspberryPiLearningReminder

## Uses awesome Duolingo API from here https://github.com/KartikTalwar/Duolingo

## Setup

**Move all files to the Documents folder on the Raspberry Pi.**

### Duolingo setup 

In duoAlert.py, change where it says username on line 6 to whatever your Duolingo username is.
Same thing where it says password; replace it with your Duolingo password. 
On line 8, feel free to change your goal amount of xp per day. 

### Scheduling (Runs every 30 minutes from 4 to 9 o'clock)

Open command prompt, and type
```bash
crontab -e
```
(if it asks what you want to use to edit, open it in nano) and add this to the bottom of it

```bash
*/30 16-21 * * * python3 /home/pi/Documents/duoAlert.py
```

You can change when the program is run by changing the beginning part ("\*/30 16-21 * * \*")
For help getting specific times, you can use this https://crontab.guru/#*/30_16-21_*_*_*_

After that is done, press ctrl+x, then press y, and finally press enter to save the new changes.

Reboot it by typing the following, and you should be good to go.
```bash
sudo reboot
```
