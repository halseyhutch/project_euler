import numpy as np


def p11(k):
    nums = np.loadtxt('data/p11.txt', dtype=int)
    res = 0
    m = nums.shape[0]
    n = nums.shape[1]
    for i in range(m):
        for j in range(n):
            # we only need to check down, right, and bottom diags
            # if we are checking every starting entry
            # down
            d = np.prod(nums[i:min(m, i+k), j])
            # right
            r = np.prod(nums[i, j:min(n, j+k)])
            # left diag
            flipped = np.fliplr(nums[i:min(m, i+k), max(0, j-k):(j+1)])
            ld = np.prod(np.diag(flipped))
            # right diag
            rd = np.prod(np.diag(nums[i:min(m, i+k), j:min(n, j+k)]))
            res = max([res, d, r, ld, rd])
    return res


print(p11(4))