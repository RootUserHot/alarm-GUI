import pygame

class music:

    def pmusic(self, file):
        pygame.init()
        pygame.mixer.init()
        pygame.time.Clock()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(3)
        return True

    def stopmusic(self):
        pygame.mixer.music.stop()

    def getmixerargs(self):
        pygame.mixer.init()
        freq, size, chan = pygame.mixer.get_init()
        return freq, size, chan

    def initMixer(self):
        BUFFER = 3072
        FREQ, SIZE, CHAN = self.getmixerargs()
        pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)