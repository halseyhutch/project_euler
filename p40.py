def p40():
    nums = "".join([str(x) for x in range(1, 200_000)])
    res = 1
    for i in [0, 9, 99, 999, 9_999, 99_999, 999_999]:
        res *= int(nums[i])
    return res


print(p40())