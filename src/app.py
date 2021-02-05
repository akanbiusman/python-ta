import sys
import os


def palindrome():
    s = input("enter a string: ").strip()

    if solution(s):
        print(s, "is a palindrome")
    else:
        print(s, "is not a palindrome")

def solution(s):
    low = 0
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1
    return True

palindrome()



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
