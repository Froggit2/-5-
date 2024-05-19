a = range(1, 21)
g = set()
f = dict()
for n in range(3, 21):
    for x in a:
        for y in a:
            if n % (x + y) == 0:
                if x != y:
                    g.add(n)
                    f[*g] = x, y
                    g.pop()
                    print(f)