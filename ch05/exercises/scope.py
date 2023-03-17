def multiply_without_multiplication(num1,num2):
    num3 = 0
    for i in range(0,num2):
        num3 += num1
    return num3

def exponent_without_exponentation(num,exp):
    return num**exp

def square(number):
    return multiply_without_multiplication(number,number)

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    result1 = multiply_without_multiplication(x,y)
    print(result1)
    result2 = exponent_without_exponentation(x,y)
    print(result2)
    result3 = square(x)
    print(result3)
    
    
main()