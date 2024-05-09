# Python (coding): debugging test

**Instructions**

You are about to go shopping for some candy in a local store.
They sell candy for either $1 or $2 a piece.
You would like to know in how many unique ways you can purchase candy based on the amount of money you have.


You have initially a function `buying_candy` that takes an integer, `amount_of_money`, and returns an integer that represents the number of unique ways to buy candy.
However, you notice that there are some bugs in your code.
**You now need to debug it.**

If `amount_of_money` is 0 or negative, then the function `buying_candy` should return 0.

Examples:

* Input 1, Output 1 : 1
* Input 2, Output 2 : 11, 2
* Input 3, Output 3 : 111, 12, 21
* Input 4, Output 5 : 1111, 112, 121, 211, 22
* Input 5, Output 8 : 11111, 1112, 1121, 1211, 2111, 122, 212, 221


* 1: 1 - 1
* 2: 2 - 11, 2
* 3: 3 - 111, 12, 21
* 4: 5 - 1111, 112, 121, 211, 22
* 5: 8 - 11111, 1112, 1121, 1211, 2111, 122, 212, 221

```python
def buying_candy( amount_of_money ) :
    if amount_of_money < 2:
		return 1
	dp = {
		0: 1,
		1: 1
	}
	x = 0
	while x < amount_of_money:
		dp[x] = dp[x] + dp[x - 1]

	return dp[amount_of_money]
```
