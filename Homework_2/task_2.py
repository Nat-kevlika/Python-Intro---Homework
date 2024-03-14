####### version 1 ###############
numb_1 = int(input("Enter the first number: "))
numb_2 = int(input("Enter the second number: "))

if numb_1 % numb_2 == 0:
    print(numb_1, " is a multiple of ", numb_2)
else:
    print(numb_1, " is not a multiple of ", numb_2)


########## version 2 ###################
# numb_1 = int(input("Enter the first number: "))
# numb_2 = int(input("Enter the second number: "))
# nat_numb = [n for n in range(1, numb_1+1)]
# print(nat_numb)
#
# if numb_1 in [numb_2 * n for n in nat_numb]:
#     print(numb_1, "is a multiple of ", numb_2)
# else:
#     print(numb_1, "is not a multiple of ", numb_2)

