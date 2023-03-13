def multiply_without_multiplication(num1,num2):
    num3 = 0
    for i in range(0,num2):
        num3 += num1
    return num3

def exponent_without_exponentation(num,exp):
    num3 = 1
    for i in range(0,exp):
        num3 *= num
    return num3

def square(number):
    return multiply_without_multiplication(number,number)

result1 = multiply_without_multiplication(5,8)
print(result1)
result2 = exponent_without_exponentation(2,7)
print(result2)
result3 = square(6)
print(result3)
