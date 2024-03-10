n = int(input("შეიყვანეთ რიცხვი შუალედში- (0 < n < 50): "))
if 0 < n < 50:
    for i in range(1, n + 1):
        gamyofebi = []
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                gamyofebi.append(j)
                count += 1
                if count == 3:
                    break
        gamyofebi_str = ' '.join(str(x) for x in gamyofebi)
        print(str(i) + " - " + gamyofebi_str)
else:
    print("შეყვანილი რიცხვი არაა მოცემულ შუალედში")
