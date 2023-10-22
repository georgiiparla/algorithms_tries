'''The idea here is that we don't need to reverse all the digits, only half the digits. The first line checks some edge cases, and returns False immediately if the number is negative or ends with a 0 (with the exception of the number 0 itself). The loop then uses the modulo and floor division operators to reverse the digits and transfer them to the half variable.

Once the halfway point is reached, we return True if the two halves are equal to each other. If the number originally had an odd number of digits, then the two halves will be off by 1 digit, so we also remove that digit using floor division, then compare for equality.'''

# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]


# print(isPalindrome(x = -121))


def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10
    return x == half or x == half // 10


print(isPalindrome(x = -121))
