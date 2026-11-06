drink = ['珍奶','紅茶','冬瓜茶']
food = ['雞排','地瓜球','烤玉米']

p1 = [60,30,25]
p2 = [80,40,50]

for i in range(len(p1)):
    for j in range(len(p2)):
        if p1[i] + p2[j] <= 100:
            print(drink[i],food[j])
            