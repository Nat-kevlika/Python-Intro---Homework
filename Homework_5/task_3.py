n = int(input("შეიყვანეთ ნაძვის ხის სიმაღლე შუალედში -  (0 < n < 50): "))

if 0 < n < 50:
    print(" " *(n) + "*")


    for i in range(1, n):
        sivrce_marcxniv = " " * (n - i - 1)
        xazi_marcxniv = "/" * i
        shuashi = " | "
        xazi_marjvniv = "\\" * i
        sivrce_marjvniv = " " * (n - i - 1)
        print(sivrce_marcxniv + xazi_marcxniv + shuashi + xazi_marjvniv + sivrce_marjvniv)


    dziri = " " * (n - 2)
    print(dziri + "  | ")
else:
    print("შეიყვანეთ რიცხვი მოცემულ შუალედში!")

