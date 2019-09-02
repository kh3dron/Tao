import random

with open ("tao.txt") as f:
    tao = f.read().split("\n")

posts  = [''] * 663
pointer = 0

for r in range(1, len(tao)-1):
    if len(tao[r]) > 4:
        posts[pointer] += " " + tao[r]
        if "." in tao[r]:
            pointer += 1

for r in range(0, len(posts)-4):
    print ((posts[r])[1:])

#test my soon-to-be gt_tao metehod in taobot.py
with open("formatted_tao.txt") as g:
    taos = g.read().splitlines()
    
print(taos[random.randint(0, 663)])
