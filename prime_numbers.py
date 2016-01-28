num = int(input("Enter number:"))

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print ("Not prime #")
            print (i, "times", num//i,"is", num)
            break
    else:
        print ("Number entered is prime")
else:
    print ("not")
        
