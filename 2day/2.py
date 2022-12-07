

k = lambda x:ord(x) - 87
f = sum([6 + k(r[1]) if "".join(r) in ["AY", "BZ", "CX"] else 3 + k(r[1]) if ord(r[0]) + 23 == ord(r[1]) else k(r[1]) for r in [k.strip().split(" ") for k in open("input.txt").readlines()]])
