def buy_and_sell_stock_once(prices):
    maximum = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maximum:
                maximum = profit
    return maximum


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


print(buy_and_sell_once(A))
