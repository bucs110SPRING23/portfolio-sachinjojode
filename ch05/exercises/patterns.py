def star_pyramid():
    rows = int(input("Please enter a number: "))
    for i in range(1, rows + 1):
        print("*" * i)

def rstar_pyramid():
    rows = int(input("Please enter a number: "))
    for i in range(rows, 0 , -1):
        print("*" * i)
    
star_pyramid()
rstar_pyramid()