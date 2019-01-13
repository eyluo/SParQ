from random import randint

class PQueue(object):
    def __init__(self):
        self.queue = list()
        self.ID = randint(0, 2**31)

    def add(self, track, position):
        if (track not in self.queue):
            self.queue.insert(position, track)

    