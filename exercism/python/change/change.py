def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    inf = float('inf')
    dp = [0] + [inf] * target
    count_coins = []
    remaining = target
    

    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    
    for coin in sorted(coins, reverse=True):
        while remaining >= coin and dp[remaining] == dp[remaining - coin] + 1:
            count_coins.append(coin)
            remaining -= coin

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    return sorted(count_coins)   
