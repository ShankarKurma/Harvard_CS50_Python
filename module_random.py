"""import random

coin = random.choice(["heads","tails"])

print(coin)
"""

#Example 2
#from random import choice
#coin = choice(["heads","tails"])
#print(coin)

#example 3
"""
import random
number = random.randint(1,10)
print(number)
"""

import random
cards = ["jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)
