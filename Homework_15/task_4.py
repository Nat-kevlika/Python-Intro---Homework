def count_vowel(v):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in v:
        if char.lower() in vowels:
            count += 1
    return count

def main():
    strings = ["Test", "Python", "banana", "apple", "ABCDE"]
    for v in strings:
        vowels = count_vowel(v)
        print(f"{v} -> {vowels}")

if __name__ == '__main__':
    main()

