from num2words import num2words
import re


def p17(limit):
    res = 0
    for i in range(1, limit + 1):
        res += len(re.sub(" |-", "", num2words(i)))
    return res


print(p17(1000))