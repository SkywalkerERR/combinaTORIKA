import itertools

words = []

with open('words-pool.txt','r', encoding='UTF-8') as f:
    for line in f.readlines():
        if '\n' in line:
            line = line[:-1]
        words.append(line)


permutations = itertools.permutations

for i in permutations(words, 12):
    print(i)

