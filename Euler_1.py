from itertools import count
from math import factorial, sqrt

triangle = [['75'],
            ['95', '64'],
            ['17', '47', '82'],
            ['18', '35', '87', '10'],
            ['20', '04', '82', '47', '65'],
            ['19', '01', '23', '75', '03', '34'],
            ['88', '02', '77', '73', '07', '63', '67'],
            ['99', '65', '04', '28', '06', '16', '70', '92'],
            ['41', '41', '26', '56', '83', '40', '80', '70', '33'],
            ['41', '48', '72', '33', '47', '32', '37', '16', '94', '29'],
            ['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14'],
            ['70', '11', '33', '28', '77', '73',
                '17', '78', '39', '68', '17', '57'],
            ['91', '71', '52', '38', '17', '14', '91',
                '43', '58', '50', '27', '29', '48'],
            ['63', '66', '04', '68', '89', '53', '67',
                '30', '73', '16', '69', '87', '40', '31'],
            ['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']]


def multiples_sum(a, b, limit):
    res = 0
    for i in range(limit):
        if (i % a == 0) or (i % b == 0):
            res += i
    return res

# print(multiples_sum(2, 10, 1000))


def fibonacci_sequence(n):
    if n < 2:
        return 1
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)


def fib_limit(limit: int, type: bool):
    fibs = [1]
    count = 2
    while fibonacci_sequence(count) < limit:
        if type:
            if (fibonacci_sequence(count) % 2 == 0):
                fibs.append(fibonacci_sequence(count))
        else:
            if (fibonacci_sequence(count) % 2 != 0):
                fibs.append(fibonacci_sequence(count))
        count += 1
    if type:
        return sum(fibs, -1)
    return sum(fibs)

# print(fib_limit(4000000, True))


def is_prime(n, type: bool):
    factors = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
    if type:
        if len(factors) > 1:
            return False
        return True
    return factors


# print(is_prime(123456789, False))


def largest_prime_factors(n):
    factors = is_prime(n, False)
    for f in factors:
        if is_prime(f, True):
            largest = f
    return largest

# print(largest_prime_factors(600851475143))


def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def largest_palindrome_product(n):
    res = 0
    for i in range(2, n):
        for j in range(2, n):
            if is_palindrome(i*j) and i*j > res:
                res = i*j
    return res

# print(largest_palindrome_product(1000))


def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)


# print(mcd(387296, 1))


def mcm(a, b):
    if (a or b) == 0:
        return 0
    return int((a*b)/mcd(a, b))

# print(mcm(21,6))


def smallest_multiple(a, b):
    res = mcm(a, a+1)
    for i in range(a+2, b):
        res = mcm(res, i)
    return res

# print(smallest_multiple(1,20))


def sum_square_difference(limit):
    sum_squares = 0
    squares_sum = 0
    for i in range(limit+1):
        sum_squares += i**2
        squares_sum += i
    squares_sum = squares_sum**2
    return squares_sum - sum_squares

# print(sum_square_difference(100))


def nst_prime(n):
    counter = 0
    prime = 1
    i = 2
    while counter != n:
        if is_prime(i, True):
            prime = i
            counter += 1
        i += 1

    return prime

# print(nst_prime(10001))


def sieve_of_erastosthenes(limit):
    arr = [i for i in range(2, limit+1)]
    i = 0
    j = 0
    # 0 1 2 3 4 5 6 7 8  9
    # 2 3 4 5 6 7 8 9 10 11
    # 2*0+1 2*1+1 2*2+1 2*3+1
    while arr[i] <= int(sqrt(limit))+1:
        p = arr[i]
        if p != 0:
            # print(f"""p {p}
            #         i {i}
            #         j {j}""")
            count = 2*p
            while count <= limit:
                if count in arr:
                    ind = arr.index(count)
                    arr.pop(ind)
                    arr.insert(ind, 0)
                count += p
        i = 2*j+1
        j += 1
    return arr


# print(sieve_of_erastosthenes(1000000))


def sieve_of_erastosthenes_enchanted(limit):
    arr = [True] * (limit+1)
    arr[0] = False
    arr[1] = False
    i = 2
    j = 1
    # 0 1 2 3 4 5
    # 0 1 2 3 4 5

    while i <= int(sqrt(limit)+1):
        if arr[i]:
            count = 2*i
            while count <= limit:
                arr[count] = False
                count += i
        i = 2*j+1
        j += 1

    return arr


# print(sieve_of_erastosthenes_enchanted(100000))


def largest_product_series(series, delta):
    largest = 0
    current = 1
    stringa = ""
    for i in range(len(series)):
        stringa = series[i:i+delta]
        for j in stringa:
            current *= int(j)
        if current > largest:
            largest = current
        current = 1
    return largest

# print(largest_product_series(BLOB, 13))


def pythagorean_triple(limit):
    res = 0
    m = 2
    n = 1
    while m != limit:
        while n < m:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a+b+c == 1000:
                res = a*b*c
                return res
            n += 1
        m += 1
        n = 1
    return False

# print(pythagorean_triple(1000))


def sum_primes(limit):
    primes = sieve_of_erastosthenes_enchanted(limit)
    sum = 0
    for i in range(len(primes)):
        if primes[i]:
            sum += i
    return sum

# print(sum_primes(2000000))


def prod(n):
    prod = 1
    for i in n:
        prod *= int(i)

    return int(prod)


def largest_grid_product(blob):
    largest = 0
    current = 0
    to_product = []
    for i in range(len(blob)):
        for j in range(len(blob[i])):
            if i > 16 and j <= 16:
                right = prod(blob[i][j:j+4])
                print(f"19-j {19-j} j = {j}")
                down = prod([blob[i+f][j] for f in range(0, (19-i))])
                x = [d for d in range(0, 19-i)]
                y = [d for d in range(0, 4)]
                diag_right = prod([blob[i+f][j+h] for f, h in zip(x, y)])
                diag_left = prod([blob[i+f][j-h] for f, h in zip(x, y)])
            elif i <= 16 and j > 16:
                right = prod(blob[i][j:j+(19-j)])
                print(f"19-j {19-j} j = {j}")
                down = prod([blob[i+f][j] for f in range(0, 4)])
                x = [d for d in range(0, 4)]
                y = [d for d in range(0, 19-j)]
                diag_right = prod([blob[i+f][j+h] for f, h in zip(x, y)])
                diag_left = prod([blob[i+f][j-h] for f, h in zip(x, y)])
            elif i > 16 and j > 16:
                right = prod(blob[i][j:j+(19-j)])
                print(f"19-j {19-j} j = {j}")
                down = prod([blob[i+f][j] for f in range(0, (19-i))])
                x = [d for d in range(0, 19-i)]
                y = [d for d in range(0, 19-j)]
                diag_right = prod([blob[i+f][j+h] for f, h in zip(x, y)])
                diag_left = prod([blob[i+f][j-h] for f, h in zip(x, y)])
            else:
                # do all things
                # right
                right = prod(blob[i][j:j+4])
                down = prod([blob[i+f][j] for f in range(0, 4)])
                print(f"i {i} j {j}")
                diag_right = prod([blob[i+f][j+f] for f in range(0, 4)])
                diag_left = prod([blob[i+f][j-f] for f in range(0, 4)])
            current = max(right, down, diag_right, diag_left)
            print(f"""
            right {right}
            down {down}
            diag_right {diag_right}
            diag_left {diag_left}
            max {max(right, down, diag_right, diag_left)}""")
            if current > largest:
                largest = current

    return largest

# print(largest_grid_product(BLOB_DUE))


def triangular_numbers(n, bk):
    # T = (n(n+1))/2
    if n in bk:
        return bk[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + triangular_numbers(n-1, bk)

# print(triangular_numbers(5))


def triangular_factors(n):
    bk = {}
    current = 0
    divisors = 0
    i = 0
    current_facts = []
    while divisors < n:
        current = triangular_numbers(i, bk)
        bk[i] = current
        current_facts = is_prime(current, False)
        divisors = len(current_facts)*2
        i += 1
    return current


# print(triangular_factors(500))


def horror_sum(orr):
    orr = map(int, orr.split("\n"))

    return str(sum(orr))[:10]


# print(horror_sum())


def max_collatz(limit):
    def collatz_count(n):
        if n in backup:
            return backup[n]
        if n % 2 == 0:
            backup[n] = 1 + collatz_count(n/2)
        else:
            backup[n] = 2 + collatz_count((current*3+1)/2)

        return backup[n]

    backup = {}
    max_lenght = 0
    res = 0
    current = 0
    for i in range(int(limit/2), limit+1):
        #     current = i
        #     while current != 1:
        #         if current % 2 == 0:
        #             current = current/2
        #             lenght += 1
        #         else:
        #             current = (current*3+1)/2
        #             lenght += 2
        if collatz_count(i) > max_lenght:
            # print(f"Prev max = {max_lenght}\n Current max = {lenght}")
            res = i
            max_lenght = collatz_count(i)

    return res


# print(max_collatz(1000000))

def count_paths(x, y):
    def factorial(n):
        if (2 or 1) == n:
            return n
        return n * factorial(n-1)

    res = int((factorial(x+y))/(factorial(x)*factorial(y)))
    return res

# print(count_paths(20, 20))

# print(sum(int(i) for i in str(2**1000)))


def number_letter_counts(limit):
    res = 0
    current = ""
    for i in range(1, limit+1):
        # current = num2words.num2words(i)
        res += len(current) - current.count("-") - current.count(" ")
    return res


# print(number_letter_counts(1000))

def shitty_triangle(triangle):
    res = 0
    next = 0
    ll = 0
    lr = 0
    rl = 0
    rr = 0
    for line in range(len(triangle)):
        start = int(triangle[line][next])
        res += start
        print(line)
        if line == 13:
            start = max(int(triangle[line+1][next]),
                        int(triangle[line+1][next+1]))
            res += start
            return res
        # print(start)
        ll = int(triangle[line+1][next]) + int(triangle[line+2][next])
        lr = int(triangle[line+1][next]) + int(triangle[line+2][next+1])
        rl = int(triangle[line+1][next+1]) + int(triangle[line+2][next+1])
        rr = int(triangle[line+1][next+1]) + int(triangle[line+2][next+2])
        # print(f"{ll}, {lr}, {rl}, {rr}\n{max(ll, lr, rl, rr)}")
        if max(ll, lr, rl, rr) == ll or max(ll, lr, rl, rr) == lr:
            pass
        else:
            next += 1

    return

# print(shitty_triangle(triangle))


def counting_sundays():
    months = {
        "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31
    }
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    sundays = 0
    i = 0
    for year in range(1900, 2001):
        if year == 1901:
            sundays = 0
        if year % 4 == 0 and year % 100 != 0:
            months["February"] = 29
            for month, lenght in months.items():
                for day in range(1, lenght+1):
                    # print(f"{day}/{month}/{year}\nToday is: {days[i]}")
                    prev = days[i]
                    if i == 6:
                        if day == 1:
                            sundays += 1
                        i = 0
                    else:
                        i += 1
            months["February"] = 28
        elif year % 100 == 0 and year % 400 == 0:
            months["February"] = 29
            for month, lenght in months.items():
                for day in range(1, lenght+1):
                    # print(f"{day}/{month}/{year}\nToday is: {days[i]}")
                    prev = days[i]
                    if i == 6:
                        if day == 1:
                            sundays += 1
                        i = 0
                    else:
                        i += 1
            months["February"] = 28
        else:
            for month, lenght in months.items():
                for day in range(1, lenght+1):
                    # print(f"{day}/{month}/{year}\nToday is: {days[i]}")
                    prev = days[i]
                    if i == 6:
                        if day == 1:
                            sundays += 1
                        i = 0
                    else:
                        i += 1

    return sundays


# print(counting_sundays())

# print(sum(int(i) for i in str(factorial(100))))
def d(n):
    divisors = is_prime(n, False)
    for i in range(len(divisors)):
        if (int(n/divisors[i]) not in divisors) and divisors[i] != 1:
            divisors.append(int(n/divisors[i]))
    divisors.pop(0)
    return sorted(divisors)


# print(d(123456789))


def amicable_numbers():
    amicable = []
    divisors = {}
    res = 0
    for i in range(1, 10001):
        divisors[i] = sum(d(i))
    for i in divisors:
        # se d(220) è uguale a d(284)
        #     284               220
        if divisors[i] < 10001 and i != 1:
            # print(f"{i} ? {divisors[divisors[i]]}")
            if i == divisors[divisors[i]] and divisors[i] != i:
                amicable.append(i)

    return sum(amicable)


# print(amicable_numbers())

def name_scores():
    txt = [i.strip('"')
           for i in open("p022_names.txt", "r").read().split(",")]
    txt.sort()
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    scored = {}
    res = 0
    current_score = 0

    for name in txt:
        name_sorted = "".join(sorted(name))
        if name_sorted in scored:
            res += scored[name_sorted] * (txt.index(name)+1)
        else:
            for letter in name:
                current_score += alphabet[letter]
            scored[name_sorted] = current_score
            res += scored[name_sorted] * (txt.index(name)+1)
            current_score = 0

    return res


# print(name_scores())


def non_abundant_sum(limit):
    def abundant_number(n):
        if sum(d(n)) > n:
            return True
        return False

    abduntants = [i for i in range(limit+1) if abundant_number(i)]
    sums = set([])

    print(abduntants)
    for i in abduntants:
        for j in abduntants:
            if i+j > limit:
                break
            sums.add(i+j)

    res = [number for number in range(limit+1) if number not in sums]

    return sum(res)


# print(non_abundant_sum(120))
