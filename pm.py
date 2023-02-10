a = int(input("Enter a number:" ))
Isprime =True
for i in range(2,a):
    if (a%i == 0):
        Isprime =False
        break

    elif (a%i != 0):
        Isprime =True
if Isprime == True:
    print('It is a prime number')
elif Isprime == False:
    print('It is not a prime number')