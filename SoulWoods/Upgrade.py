import random
class UpgradeClass:
    def __init__(self, ROUNDCOUNTER):
        self.instance = ROUNDCOUNTER
        self.heilung = int (random.uniform(1,100)+ROUNDCOUNTER)
        self.damageBuff = int (random.uniform(1,20)+ROUNDCOUNTER)
        self.speedBuff = int (random.uniform(1,20)+ROUNDCOUNTER)