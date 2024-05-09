dp = [1, 1]


def buying_candy(amount_of_money):
    if amount_of_money < 1:
        return 0
    elif amount_of_money == 1:
        return 1

    for x in range(len(dp), amount_of_money + 1):
        dp.append(dp[x - 2] + dp[x - 1])

    return dp[amount_of_money]


# 1: 1 - 1
# 2: 2 - 11, 2
# 3: 3 - 111, 12, 21
# 4: 5 - 1111, 112, 121, 211, 22
# 5: 8 - 11111, 1112, 1121, 1211, 2111, 122, 212, 221

data = [
    (-5, 0),
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21),
]

for money, expected in data:
    ways = buying_candy(money)
    print("money", money, "expected", expected, "actual", ways)
