"""
Kő    A: 0 | B 
Papír B: 1 | C
Olló  C: 2 | A

"""


k = lambda x,l: ((ord(x) -65) + l) % 3
print(sum([ {"X":k(r[0],2)+1, "Y":k(r[0],0) + 4, "Z":k(r[0],1)+7}[r[1]] for r in [rr.strip().split(" ") for rr in open("input.txt").readlines()]]))
