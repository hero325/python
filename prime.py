
num = int(input("Enter a number: "))  #to enter a number
def primecheck(num):  
    if num > 1:  #number can never be negative
        for j in range(2,num):  
            if (num % j) == 0:  
                print(num,"is not a prime number")
                print("Try new number")
                print(j,"times",num//j,"is",num)
                break  
            else:  #if number is not divisible then it is a prime number
                print(num,"is a prime number")  
    else:  
        print(num,"is not a prime number")  #if number is negative it is not a prime number
primecheck(num)

