import random
class Monster:
    playerLevel = int (0)
    monsterHP = int (random.uniform(1,100)+100)
    monsterSpeed = int (random.uniform(1,20)+1)
    monsterDamage = int (random.uniform(1,10)+6)
    
    