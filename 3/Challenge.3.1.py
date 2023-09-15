# 랜덤 동물 만들기

import random

adjectives = ["귀여운", "용맹한", "예쁜", "무서운", "깜찍한", "잔망스러운", "요망한"]
animals = ["🐭", "🐮", "🐯", "🐰", "🐲", "🐍", "🐴", "🐏", "🐵", "🐔", "🐶", "🐷"]

randomAdjective = random.choice(adjectives)
randomAnimal = random.choice(animals)

print(randomAdjective, randomAnimal)