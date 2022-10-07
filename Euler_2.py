from concurrent.futures import process
from turtle import back, pos
from typing import Optional
from unittest import result
from Euler_1 import fibonacci_sequence, is_prime, mcd, sieve_of_erastosthenes_enchanted
from math import sqrt


def permutation_ordered(current: list):
    perms = ["".join(current)]

    while True:
        curr_k = -1
        curr_i = -1
        for k in range((len(current)-1)):
            if current[k] < current[k+1]:
                if k > curr_k:
                    curr_k = k
        if curr_k == -1:
            break
        for i in range(len(current)):
            if current[curr_k] < current[i]:
                if i > curr_i:
                    curr_i = i
        current[curr_k], current[curr_i] = current[curr_i], current[curr_k]
        current = current[:curr_k+1] + current[curr_k+1:][::-1]
        perms.append("".join(current))

    return perms


# print(permutation_ordered(["a", "b", "c"]))


def fibonacci_blob(lenght):
    fibs = [1, 1]
    index = 3

    while True:
        temp = fibs[0]
        fibs[0] = fibs[1]
        fibs[1] = temp + fibs[0]
        if len(str(fibs[1])) >= lenght:
            break
        index += 1

    return index


# print(fibonacci_blob(1000))

def longest_period(limit):
    def period(p):
        t = 0
        r = 1
        n = 0
        while True:
            t += 1
            x = r * 10
            d = int(x / p)
            r = x % p
            n = n*10 + d
            if r == 1:
                break
        if t == p-1:
            return n
        return False

    longest = 0
    res = 0

    for p in range(2, limit):
        if is_prime(p, True) and 10 % p != 0:
            curr = period(p)
            if curr and len(str(curr)) > longest:
                longest = len(str(curr))
                res = p
    return res


# print(longest_period(1000))

def quadratic_primes():
    # n^2 + an + b
    counter = 0
    current = 0
    max_score = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            while True:
                current = counter ** 2 + a*counter + b
                if current <= 1:
                    if counter > max_score:
                        max_score = counter
                        max_a = a
                        max_b = b
                    counter = 0
                    break
                elif not is_prime(current, True):
                    if counter > max_score:
                        max_score = counter
                        max_a = a
                        max_b = b
                    counter = 0
                    break
                counter += 1

    return max_a*max_b


# print(quadratic_primes())

def spiral_grid():
    delta_corner = 2
    result = 4
    current = 3
    i = 1

    while current != 1002001:
        current += delta_corner
        result += current
        i += 1
        if i == 4:
            delta_corner += 2
            i = 0

    return result


# print(spiral_grid())

def distinct_powers():
    powers = set([])

    for a in range(2, 101):
        for b in range(2, 101):
            powers.add(a**b)

    return len(powers)


# print(distinct_powers())

def digit_fifth_powers():
    result = []

    for i in range(2, 1000000000):
        current = 0
        for j in str(i):
            current += int(j)**5
        if current == i:
            result.append(i)

    return result


def coin_sums():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    count = 0
    target = 200

    for a in range(target, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                for h in range(g, -1, -1):
                                    if h == 0:
                                        count += 1

    return count


# print(coin_sums())

def possible_divisors(n, divs):
    result = []

    for i in divs:
        if sorted(f"{(int(n)//int(int(i)))}{n}{int(i)}") == list("123456789"):
            result.append(int(i))

    return result


# print(possible_divisors("7254", is_prime(7254, False)))


def pandigital_number():
    results = []

    for i in range(0, 10000):
        divisors = possible_divisors(str(i), is_prime(i, False))
        if len(divisors):
            results.append(i)

    return sum(results)


# print(pandigital_number())

def digit_cancelling_fractions():
    fractions = []
    numerator = 1
    denominator = 1

    for b in range(1, 10):
        for a in range(1, 10):
            for c in range(1, 10):
                base = a/c
                completed = int(f"{a}{b}")/int(f"{c}{b}")
                completed_one = int(f"{a}{b}")/int(f"{b}{c}")
                completed_two = int(f"{b}{a}")/int(f"{c}{b}")
                completed_three = int(f"{b}{a}")/int(f"{b}{c}")
                if base == completed and base < 1:
                    numerator *= int(f"{a}{b}")
                    denominator *= int(f"{c}{b}")
                elif base == completed_one and base < 1:
                    numerator *= int(f"{a}{b}")
                    denominator *= int(f"{b}{c}")
                elif base == completed_two and base < 1:
                    numerator *= int(f"{b}{a}")
                    denominator *= int(f"{c}{b}")
                elif base == completed_three and base < 1:
                    numerator *= int(f"{b}{a}")
                    denominator *= int(f"{b}{c}")

    result = mcd(numerator, denominator)
    result = denominator // result

    return result


# print(digit_cancelling_fractions())

def digit_factorial():
    factorials = {"0": 1, "1": 1, "2": 2, "3": 6, "4": 24,
                  "5": 120, "6": 720, "7": 5040, "8": 40320, "9": 362880}
    results = []
    value = 0

    for i in range(3, 10000000):
        current = str(i)
        for j in current:
            value += factorials[j]
            if value > i:
                break
            if value == i:
                results.append(i)
        value = 0

    return results


# print(digit_factorial())

def rotatate_generator(n, i=0, res=0):
    if not len(n):
        return None
    if i > len(n):
        if i == res:
            return True
        return False
    if is_prime(int(n), True):
        res += 1

    new_n = n[1:] + n[:1]
    res = rotatate_generator(new_n, i+1, res)

    return res


# print(rotatate_generator("19937"))


def circular_primes(limit):
    to_analyze = dict(zip([str(i) for i in range(0, limit)],
                          sieve_of_erastosthenes_enchanted(limit)))
    count = 0
    i = 2
    j = 1

    while i < limit:
        if to_analyze[str(i)]:
            if rotatate_generator(str(i)):
                count += 1
        i = 2*j+1
        j += 1

    return count


print(circular_primes(1000000))
