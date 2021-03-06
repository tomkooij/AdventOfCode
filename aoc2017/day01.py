
with open('input/input01.txt') as f:
    s = f.read()

    x = 0
    for a, b in zip(s, s[1:]+s[0]):
        if a == b:
            x += int(a)
    print('part a:', x)

    y = 0
    half = len(s) // 2
    for a, b in zip(s[:half], s[half:]):
        if a == b:
            y += 2*int(a)
    print('part b:', y)


# code golf. disregarding length of filename and keeping spaces/formatting 
a = open("input\input01.txt").read()
h = len(a) // 2
print(sum([int(i) for i,j in zip(a,a[1:]+a[0]) if i == j]),
      sum([int(i) for i,j in zip(a,a[h:]+a[:h]) if i == j]))
