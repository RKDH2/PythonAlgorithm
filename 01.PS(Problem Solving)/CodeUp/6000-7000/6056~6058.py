# 6056
a, b = map(lambda x: bool(int(x)), input().split())
print((a and (not b)) or ((not a) and b))

# 6057
a, b = map(lambda x: bool(int(x)), input().split())
print((a and b or (not a and not b)))

# 6058
a, b = map(int, input().split())

if not a and not b:
    print(True)
else:
    print(False)