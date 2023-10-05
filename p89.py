import re

with open('data/p89.txt') as f:
    nums = f.read().splitlines()

sol = 0
for num in nums:
    orig = num
    # clean up 4s
    num = re.sub('IIII', 'IV', num)
    num = re.sub('XXXX', 'XL', num)
    num = re.sub('CCCC', 'CD', num)
    # clean up 9s
    num = re.sub('VIV', 'IX', num)
    num = re.sub('LXL', 'XC', num)
    num = re.sub('DCD', 'CM', num)
    sol += (len(orig) - len(num))
print(sol)
