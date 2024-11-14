"""A function that returns max profit achievable"""
prices = [1, 2, 8, 10, 20, 26] # a list of stock prices where the index represents the days 
LENGTH = len(prices)
def max_profit(prices):
    new_profit = 0
    for i in range(LENGTH):
        buy = prices[i]            
        for j in range (i+1, LENGTH):
            sell = prices[j]
            profit = sell - buy
            if  profit > new_profit:
                new_profit = profit
    return new_profit
print(max_profit(prices))
