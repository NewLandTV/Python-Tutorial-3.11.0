def Func():
    print("Func!")

def PrintTriangle():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print("*", end = "")

        print("")

def GetName():
    return "장경혁tv"

def SetAndShow(newX):
    x = newX

    print(x)

Func()

SetAndShow("Hello Function!")

print(GetName())    # print("장경혁tv")

for i in range(1, 10):
    PrintTriangle()