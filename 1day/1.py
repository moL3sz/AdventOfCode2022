

print(max(map(lambda x: sum(map(int,x.split("\n"))), open("./input.txt").read().split("\n\n"))))
