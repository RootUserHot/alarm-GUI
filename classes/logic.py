from .music import *
import time

class logic(music):

    def alarm(self, h, m, day):
        if len(h) == 1: h = '0' + h
        if len(m) == 1: m = '0' + m
        while True:
            time.sleep(1)
            if int(m) <= int(time.strftime("%M")) and str(day) == str(time.strftime("%p")):
                if int(h) <= int(time.strftime("%I")):
                    return True

    def startMusic(self):
        m = music()
        m.initMixer()
        file = 'source/music/alarm.wav'
        m.pmusic(file)