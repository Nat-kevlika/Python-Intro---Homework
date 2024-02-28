####### version 1 ###############
Numb_1 = int(input("Enter the first number: "))
Numb_2 = int(input("Enter the second number: "))

if Numb_1 % Numb_2 == 0:
    print(Numb_1, " is a multiple of ", Numb_2 )
else:
    print(Numb_1, " is not a multiple of ", Numb_2)


########## version 2 ###################
Numb_1 = int(input("Enter the first number: "))
Numb_2 = int(input("Enter the second number: "))
nat_numb = [n for n in range(1, Numb_1+1)]
print(nat_numb)

if Numb_1 in [Numb_2 * n for n in nat_numb]:
    print(Numb_1, "is a multiple of ", Numb_2)
else:
    print(Numb_1, "is not a multiple of ", Numb_2)



