import math
n = int(input())
ring_r = list(map(int, input().split()))
ring_1 = ring_r[0]
for i in range(1, len(ring_r)):
    r_gcd = math.gcd(ring_1, ring_r[i])
    A = ring_1 // r_gcd
    B = ring_r[i] // r_gcd
    print(f'{A}/{B}')