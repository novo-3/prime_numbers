num = int(input("Enter number:"))

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print ("The number you entered is not a prime #")
            print (i, "times", num//i,"is", num)
            break
    else:
        print ("Bingo! Number entered is a prime #")
else:
    print ("not hot")
        
