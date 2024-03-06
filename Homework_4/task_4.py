n = int(input('შეიყვანეთ არაუარყოფითი მთელი რიცხვი, შუალედში ( 0 <= n < 20): '))

if 0 <= n < 20:
    pirveli = 0
    meore = 1
    mimdinare = 0

    if n == 0:
        mimdinare = pirveli
    elif n == 1:
        mimdinare = meore
    else:
        for i in range(2, n+1):
            mimdinare = pirveli + meore
            pirveli = meore
            meore = mimdinare

    print("მიმდევრობის n-ური წევრია: ", mimdinare)
else:
    print('შეიყვანეთ არაუარყოფითი მთელი რიცხვი, შუალედში ( 0 <= n < 20): ')



