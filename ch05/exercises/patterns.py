def star_pyramid():
    rows = int(input("Please enter a number: "))
    for i in range(rows + 1):
        print("*" * i)

def rstar_pyramid():
    rows = int(input("Please enter a number: "))
    rows1 = rows
    print("")
    for i in range(rows + 1):
        print("*" * rows1)
        rows1 -= 1
    
star_pyramid()
rstar_pyramid()