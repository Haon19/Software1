
import random

dice = int(input("enter number of dice pairs to role: "))
g = 0
j = 0
h = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
for i in range(dice):
    x = random.randint(1,6) + random.randint(1,6)
    if x == 2:
        j = j + 1
    if x == 3:
        g = g + 1
    if x == 4:
        h = h + 1
    if x == 5:
        k = k + 1
    if x == 6:
        l = l + 1
    if x == 7:
        m = m + 1
    if x == 8:
        n = n + 1
    if x == 9:
        o = o + 1
    if x == 10:
        p = p + 1
    if x == 11:
        q = q + 1
    if x == 12:
        r = r + 1
    i += 1
J = j/dice
G = g/dice
H = h/dice
K = k/dice
L = l/dice
M = m/dice
N = n/dice
O = o/dice
P = p/dice
Q = q/dice
R = r/dice
print(f"{J:.2%} {G:.2%} {H:.2%} {K:.2%} {L:.2%} {M:.2%} {N:.2%} {O:.2%} {P:.2%} {Q:.2%} {R:.2%} ")