wall = [45, 61, 27, 38, 50, 74, 63, 19, 56, 62, 82, 36]
list_answers = []

for i in range(len(wall)):
    for j in range(i+1, len(wall)):
        if wall[i] + wall[j] == 100:
            list_answers.append((wall[i], wall[j]))

print("密碼:",list_answers)