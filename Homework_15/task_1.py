def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def main():
    cels_temp = [20, 25, 40]
    fahr_temp = [celsius_to_fahrenheit(temp) for temp in cels_temp]
    print("Celsius to Fahrenheit:")
    for i in range(len(cels_temp)):
        print(f"{cels_temp[i]} C is {fahr_temp[i]} F.")

    fahr_temp = [77, 133, 100]
    cels_temp = [fahrenheit_to_celsius(temp) for temp in fahr_temp]
    print("Fahrenheit to Celsius:")
    for i in range(len(fahr_temp)):
        print(f"{fahr_temp[i]} F is {cels_temp[i]} C.")

if __name__ == '__main__':
    main()
