
from string import ascii_lowercase, ascii_uppercase;
f = sum([ascii_uppercase.index(s) + 27 if s.isupper() else ascii_lowercase.index(s)+1 for s in [tuple(set(r[:len(r)//2]) & set(r[len(r)//2:]))[0] for r in [ row.strip() for row in open("input.txt").readlines()]]])
print(f)