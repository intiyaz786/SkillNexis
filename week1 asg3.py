"""Even/Odd & Prime Number Checker."""
def check_number(num):
    if num%2==0:
        print("Even number")
    else:
        print("Odd  number")
    if num<2:
        print("Is not prime")
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                print("Is not prime")
                break
            else:
                print("Is prime")

number=int(input("Enter a number: "))
check_number(number)