from os import remove
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
