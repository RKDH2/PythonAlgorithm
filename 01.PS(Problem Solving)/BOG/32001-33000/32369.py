n, a, b = map(int, input().split())

a_onion = 1
b_onion = 1

for i in range(n):
    a_onion += a
    b_onion += b

    if a_onion < b_onion:
        a_onion, b_onion = b_onion, a_onion

    if a_onion == b_onion:
        b_onion -= 1

print(a_onion, b_onion)
