# 6 has to be the first digit.
# the remaining outer digits have to be greater and the inner five less.
# total must be sum(6:10) + 2*sum(1:5) = 70.
# therefore each arm must sum to 14.

# the arms are the following:
# (6, 5, 3) or (6, 3, 5)
# (7, 3, 4) or (7, 4, 3) or (7, 5, 2) or (7, 2, 5)
# (8, 2, 4) or (8, 4, 2) or (8, 5, 1) or (8, 1, 5)
# (9, 2, 3) or (9, 3, 2) or (9, 4, 1) or (9, 1, 4)
# (10, 1, 3) or (10, 3, 1)

# don't even really need code for this one. trying 653 first since it's higher.
# then we have to use 10 to link the 3. rest follows using 'greedy' approach.
# (6, 5, 3), (10, 3, 1), (9, 1, 4), (8, 4, 2), (7, 2, 5)
# 6531031914842725