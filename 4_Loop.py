x = 0

while x < 10:
    print(x)

    x = x + 1

for i in range(1, 10):
    print(i)
    print("For In")

print("For Out")
print("Square")

# 정사각형
for i in range(1, 6):
    print("**********")

print("Triangle")

# 삼각형
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end = "")
    
    print("")