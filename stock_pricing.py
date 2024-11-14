"""A function that returns max profit achievable"""
prices = [1, 2, 8, 10, 20, 26] # a list of stock prices where the index represents the days
LENGTH = len(prices)
def max_profit(prices):
    maximum_profit = 0
#in this for loop we choose the day to buy on
    for i in range(LENGTH):
        buy = prices[i]
#in this for loop we choose the day to sell on and then compare the profit that can be made
        for j in range (i + 1, LENGTH):
            sell = prices[j]
            profit = sell - buy
            if  profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit
print(max_profit(prices))
