import random
class Monster:
    def __init__(self, ROUNDCOUNTER):
        self.instance = ROUNDCOUNTER
        self.monsterLevel = int (0)
        self.monsterHP = int (random.uniform(1,1000)+self.instance)
        self.monsterSpeed = int (random.uniform(1,100)+self.instance)
        self.monsterDamage = int (random.uniform(1,50)+self.instance)