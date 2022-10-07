from distutils.command.build import build
from itertools import combinations
from multiprocessing import current_process
from operator import sub
from os import remove
import this
from typing import final


def letter_permutations(letters):
    def list_to_str(s):
        result = ""
        for i in s:
            result += i
        return result

    def swap(i, j, array):
        array[i], array[j] = array[j], array[i]
        return array

    def backtracking_permutation(i, k, current, results):
        if (i == k-1):
            results.append(list_to_str(current))
            return results

        for a in range(i, len(current)):
            current = swap(i, a, current)
            backtracking_permutation(i+1, k, current, results)
            current = swap(i, a, current)

        return results

    return backtracking_permutation(0, len(letters), letters, [])


# print(letter_permutations(["a", "b", "c"]))


def all_klenght_permutation(letters, k, current, results):
    def list_to_str(s):
        result = ""
        for i in s:
            result += i
        return result

    if k == 0:
        results.append(list_to_str(current))
        return results

    for i in range(len(letters)):
        new_current = ""

        new_current = current + letters[i]
        all_klenght_permutation(letters, k-1, new_current, results)

    return results


# print(all_klenght_permutation(["a", "b", "c", "d"], 3, "", []))

def recursive_palindrome(last, to_analyze):
    if to_analyze[0] != to_analyze[last]:
        return False

    if 0 == last or (last-1 == 0 and to_analyze[0] == to_analyze[last]):
        return True

    recursive_palindrome(len(to_analyze)-3, to_analyze[1:-1])
    return True


# print(recursive_palindrome(len("niti")-1, "itin"))

def remove_adiacent_same(to_analyze, pivot=0, k=1, final=""):

    if pivot+k == len(to_analyze):
        final += to_analyze[pivot]
        return final

    if to_analyze[pivot] == to_analyze[pivot+k]:
        final = remove_adiacent_same(to_analyze, pivot, k+1, final)
    if to_analyze[pivot] != to_analyze[pivot+k]:
        final += to_analyze[pivot]
        final = remove_adiacent_same(to_analyze, pivot+k, 1, final)

    return final

# print(remove_adiacent_same("AABBBCDDD"))


def reverse_string(stringa, first_half="", second_half="", i=0):
    if len(first_half) == (len(stringa)//2):
        stringa = first_half + second_half
        return stringa

    first_half = stringa[(len(stringa)//2)+i] + first_half
    second_half = second_half + stringa[(len(stringa)//2)-i-1]
    final = reverse_string(stringa, first_half, second_half, i+1)
    return final


# print(reverse_string("Techie Delight"))

def strstr(x, y, pivot=0, k=0):
    # Sample x "Techie Delight"
    # Sample y "light"
    if len(y) == 0:
        return x

    if len(y) == k:
        return pivot-k

    if x[pivot] != y[k]:
        final = strstr(x, y, pivot+1, 0)
    if x[pivot] == y[k]:
        final = strstr(x, y, pivot+1, k+1)

    return final


# print(strstr("Delight", ""))

def rotated_palidrome(to_analyze, i=0):
    # ABCDCBA
    # CBAABCD
    if not len(to_analyze):
        return False

    if i > len(to_analyze):
        return f"False, is not a rotation of any palindrome"

    if recursive_palindrome(len(to_analyze)-1, to_analyze):
        return f"True, is a rotation of {to_analyze}"

    to_analyze = to_analyze[1:] + to_analyze[:1]
    result = rotated_palidrome(to_analyze, i+1)

    return result


# print(rotated_palidrome(""))

def recursion_parentesis(n, result=set(), open_b=0, current=""):
    if n & 1 and not open_b:
        return result

    if n == 0:
        if not open_b:
            result.add(current)
        return result

    if open_b > n:
        return result

    result = recursion_parentesis(n-1, result, open_b+1, current + "(")

    if open_b > 0:
        result = recursion_parentesis(n-1, result, open_b-1, current + ")")

    return result


# print(recursion_parentesis(6))

def all_combination(a, b, c, i=0, j=0, k=0, result=[], current=""):
    # list 1 —> [John, Emma]
    # list 2 —> [Plays, Hates, Watches]
    # list 3 —> [Cricket, Soccer, Chess]
    if len(a) == i:
        return result

    if j == len(b)-1 and k == len(c):
        return all_combination(a, b, c, i+1, 0, 0, result, current)

    if k == len(c):
        return all_combination(a, b, c, i, j+1, 0, result, current)

    current = f"{a[i]} {b[j]} {c[k]}"
    result = all_combination(a, b, c, i, j, k+1, result, current)
    result.append(current)

    return result


a = ["John", "Emma"]
b = ["Plays", "Hates", "Watches"]
c = ["Cricket", "Soccer", "Chess"]


# print(all_combination(a, b, c))

def substring_gen(string, result=[]):
    if not string:
        print(result)
        return result

    for i in range(len(string)):
        result.append(string[:i+1])
        substring_gen(string[i+1:], result)
        result.pop()

    return result

# print(substring_gen("string"))
