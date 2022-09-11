from Euler_1 import fibonacci_sequence, is_prime


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

    return perms[999999]


# print(permutation_ordered([1, 2, 3]))

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


print(spiral_grid())
