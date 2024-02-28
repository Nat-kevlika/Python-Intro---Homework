Numb = int(input("Enter a integer number (max 10): "))
if Numb < 1 or Numb > 10:
    print("oups")
else:
    mart_ricx = [2, 3, 5, 7]
    gamyofebi = []

    for gamyofi in mart_ricx:
        if Numb % gamyofi == 0:
            gamyofebi = gamyofebi + [str(gamyofi)]
    if gamyofebi:
        print("mart_gamy:", ", ".join(gamyofebi))
    else:
        print("ar aqvs mart_gamy")


