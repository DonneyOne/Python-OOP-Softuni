def Generate_Rhomb(index, n):
    indent = " " * (n - index - 1)
    stars = "* " * (index + 1)
    return f"{indent}{stars}"


def Rhombus(n):
    for i in range(n):
        print(Generate_Rhomb(i, n))
    for i in range(n - 2, -1, -1):
        print(Generate_Rhomb(i, n))


Rhombus(6)
