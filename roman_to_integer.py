'''Method 1:
This solution takes the approach incorporating the general logic of roman numerals into the algorithm. We first create a dictionary that maps each roman numeral to the corresponding integer. We also create a total variable set to 0.

We then loop over each numeral and check if the one after it is bigger or smaller. If it's bigger, we can just add it to our total. If it's smaller, that means we have to subtract it from our total instead.

The loop stops at the second to last numeral and returns the total + the last numeral (since the last numeral always has to be added)'''

def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
        return total + roman[s[-1]]
    
'''Method 2:
This solution takes the approach of saying "The logic of roman numerals is too complicated. Let's make it easier by rewriting the numeral so that we only have to add and not worry about subtraction.

It starts off the same way by creating a dictionary and a total variable. It then performs substring replacement for each of the 6 possible cases that subtraction can be used and replaces it with a version that can just be added together. For example, IV is converted to IIII, so that all the digits can be added up to 4. Then we just loop through the string and add up the total.'''

# class Solution(object):
#     def romanToInt(self, s):
#         roman = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         total = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for symbol in s:
#             total += roman[symbol]
#         return total
