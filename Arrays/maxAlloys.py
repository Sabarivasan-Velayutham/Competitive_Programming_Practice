
# ### Problem Statement

# A foundry in Hackerland produces an alloy using `n` different metals. In the manufacturing of an alloy, 
# the composition of each metal is fixed, where the required quantity of each metal to produce 1 unit of the alloy 
# is denoted by `composition[i]`. The company already has `stock[i]` units of each metal in their inventory.

# The company has a budget to purchase additional metals if needed. The cost of each metal is `cost[i]` per unit. 
# The task is to find the maximum number of alloy units the company can produce using the available stock and
#  any additional metals that can be purchased within the given budget.

# **Note**: The supplier has an infinite supply of all metal types.

# ### Example

# **Input:**
# - Number of metal types, `n = 2`
# - Required composition: `composition = [1, 2]`
# - Available stock: `stock = [0, 1]`
# - Purchase cost: `cost = [1, 1]`
# - Budget: `budget = 3`

# **Output:**
# - Maximum units of alloy: `1`

# **Explanation:**
# - **Cost for 1 unit:**
#   - Required quantity: `[1, 2]`
#   - Available stock: `[0, 1]`
#   - Extra metal requirements: `[1, 1]`
#   - Cost: `(1 x 1) + (1 x 1) = 2` (within the budget)
  
# - **Cost for 2 units:**
#   - Required quantity: `[2, 4]`
#   - Available stock: `[0, 1]`
#   - Extra metal requirements: `[2, 3]`
#   - Cost: `(2 x 1) + (3 x 1) = 5` (beyond the budget)

# Thus, the maximum number of units that can be produced is `1`.

# ### Function Description

# Complete the function `findMaximumAlloyUnits` with the following parameters:

# - **int composition[n]:** The composition of metals in 1 unit of alloy.
# - **int stock[n]:** The units of each metal type that the company has in stock.
# - **int cost[n]:** The costs of each metal type.
# - **int budget:** The total money the company can spend.

# **Returns:**
# - **int:** The maximum number of alloy units that can be produced.

# ### Input Format

# 1. The first line contains an integer `n`, the number of elements in the array `composition`.
# 2. Each of the next `n` lines contains an integer representing `composition[i]`.
# 3. The next line contains an integer `n`, the number of elements in the array `stock`.
# 4. Each of the next `n` lines contains an integer representing `stock[i]`.
# 5. The next line contains an integer `n`, the number of elements in the array `cost`.
# 6. Each of the next `n` lines contains an integer representing `cost[i]`.
# 7. The last line contains an integer `budget`.

# ### Sample Case 1

# **Input:**

# ```
# 3
# 2
# 1
# 2
# 3
# 1
# 0
# 0
# 3
# 2
# 2
# 1
# 14
# ```

# **Output:** `2`

# **Explanation:**

# - **Cost for 2 units:**
#   - Required quantity: `[4, 2, 4]`
#   - Stock: `[1, 0, 0]`
#   - Extra metal requirements: `[3, 2, 4]`
#   - Cost: `(3 x 2) + (2 x 2) + (4 x 1) = 14` (within the budget)
  
# - **Cost for 3 units:**
#   - Required quantity: `[6, 3, 6]`
#   - Stock: `[1, 0, 0]`
#   - Extra metal requirements: `[5, 3, 6]`
#   - Cost: `(5 x 2) + (3 x 2) + (6 x 1) = 22` (beyond the budget)

# So, the maximum number of units that can be produced is `2`.

# ### Sample Case 2

# **Input:**

# ```
# 4
# 2
# 2
# 3
# 1
# 4
# 3
# 2
# 1
# 4
# 4
# 2
# 3
# 1
# 6
# 30
# ```

# **Output:** `3`

# **Explanation:**

# - **Cost for 3 units:**
#   - Required quantity: `[6, 6, 9, 3]`
#   - Stock: `[3, 2, 1, 4]`
#   - Extra metal requirements: `[3, 4, 8, 0]`
#   - Cost: `(3 x 2) + (4 x 3) + (8 x 1) + (0 x 6) = 26` (within the budget)
  
# - **Cost for 4 units:**
#   - Required quantity: `[8, 8, 12, 4]`
#   - Stock: `[3, 2, 1, 4]`
#   - Extra metal requirements: `[5, 6, 11, 0]`
#   - Cost: `(5 x 2) + (6 x 3) + (11 x 1) + (0 x 6) = 39` (beyond the budget)

# So, the maximum number of units that can be produced is `3`.

# --- 


def canProduceAlloys(units, composition, stock, cost, budget):
    total_cost = 0
    for i in range(len(composition)):
        required_metal = composition[i] * units
        if required_metal > stock[i]:
            total_cost += (required_metal - stock[i]) * cost[i]
        if total_cost > budget:
            return False
    return total_cost <= budget

def findMaximumAlloyUnits(composition, stock, cost, budget):
    low, high = 0, 10**9
    max_units = 0

    while low <= high:
        mid = (low + high) // 2
        if canProduceAlloys(mid, composition, stock, cost, budget):
            max_units = mid
            low = mid + 1
        else:
            high = mid - 1

    return max_units 


# Sample Test Case 1
composition = [2, 1, 2]
stock = [1, 0, 0]
cost = [2, 2, 1]
budget = 14
print(findMaximumAlloyUnits(composition, stock, cost, budget))  # Output: 2

# Sample Test Case 2
composition = [2, 2, 3, 1]
stock = [3, 2, 1, 4]
cost = [2,3,1,6]
budget = 30
print(findMaximumAlloyUnits(composition, stock, cost, budget))  # Output: 3

