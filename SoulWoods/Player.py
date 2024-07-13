import random
class Player:
    playerLevel = int (0)
    playerXP = int (0)
    playerHP = int (random.uniform(1,500)+500)
    playerSpeed = int (random.uniform(1,100)+10)
    playerDamage = int (random.uniform(1,50)+20)
    playerFleeCounter = int (3)