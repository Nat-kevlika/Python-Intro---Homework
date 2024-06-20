def create_seq_norm(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

cache = {}
def create_seq_cached(n):
    if n not in cache:
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            sequence.append(n)
        cache[n] = sequence
    return cache[n]

def main():
    n = int(input("Enter a number: "))
    print("by normal function:", create_seq_norm(n))
    print("by cached function:", create_seq_cached(n))

if __name__ == "__main__":
    main()
