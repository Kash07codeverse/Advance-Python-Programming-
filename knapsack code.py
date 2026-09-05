# 0/1 Knapsack Problem using Dynamic Programming

# Accept number of items
n = int(input("Enter the number of items: "))

# Accept weights and values
weights = []
values = []

print("\nEnter the weight of each item:")
for i in range(n):
    weight = int(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("\nEnter the value of each item:")
for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    values.append(value)

# Accept bag capacity
capacity = int(input("\nEnter the capacity of the bag: "))

# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # If item can fit in the bag
        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )

        # If item cannot fit
        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum obtainable value
print("\nMaximum obtainable value =", dp[n][capacity])