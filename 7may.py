"""def hugeTransactions(transaction):
    return abs(transaction) >= 50000

transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
bigTransactions = []

for i in transactions:
    if hugeTransactions(i) == True:
        bigTransactions.append(i)

print(bigTransactions)        """


def absoluteTotal(a, b):
    return abs(a) + abs(b)

transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
# april = [10, -10, 20, -20]
# print(absoluteTotal(10, -10))
# Use above function and the list of transaction, use the topics taught (especially for loop) and write your code below to get total amount transacted.
sum = 0
for i in transactions:
    sum = absoluteTotal(sum,i)
print(sum)