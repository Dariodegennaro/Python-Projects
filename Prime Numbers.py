
def prime_num(limit):
    for number in range (1, limit):
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number)


prime_num(int(input("Calculate the prime numbers between 1 and ")))