import random
class Player:
    playerLevel = int (0)
    playerXP = int (0)
    playerHP = int (random.uniform(1,100)+100)
    playerSpeed = int (random.uniform(1,30)+1)
    playerDamage = int (random.uniform(1,20)+6)
    playerFleeCounter = int (3)
    