numb = int(input("Enter a integer number (max 10): "))
if numb < 1 or numb > 10:
    print("oups")
else:
    mart_ricx = [2, 3, 5, 7]
    gamyofebi = []

    for gamyofi in mart_ricx:
        if numb % gamyofi == 0:
            gamyofebi = gamyofebi + [str(gamyofi)]
    if gamyofebi:
        print("mart_gamy:", ", ".join(gamyofebi))
    else:
        print("ar aqvs mart_gamy")


