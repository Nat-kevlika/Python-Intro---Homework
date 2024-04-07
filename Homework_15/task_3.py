def rev_string(s):
    if len(s) <= 1:
        return s
    else:
        return rev_string(s[1:]) + s[0]

def main():
    test_strings = ["ABC", "test", "level","mom", "wow", "Python", "racecar", "noon", "banana", ""]
    for s in test_strings:
        reversed_str = rev_string(s)
        print(f"{s}' -> '{reversed_str}'.")

if __name__ == '__main__':
    main()

