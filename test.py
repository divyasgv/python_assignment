num=int(input("Enter a Number:"))
factorial=1
if num<0:
    print("Factorial does not exist for Nagative Numbers") 
elif num==0:
        print("The factorial is 0 and 1")
else:
            for i in range(1,num+1):
                factorial=factorial*i
                print("The Factorial of",num,"is",factorial)