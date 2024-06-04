def fewestweights( weights, total):

    dp = [float('inf')] * (total + 1)
    dp[0] = 0 

    for i in weight:
        for current_total in range(i, total + 1):
            min(dp[current_total], dp[current_total - i] + 1)
            return dp[total] if dp[total] != float('inf') else -1 

if __name__ == '__main__':
    inputs = input().split()
    total = int(inputs[0])
    weight = list(map(int, inputs[1:]))

    print(f"The total of {total} pounds can be made with a minimum of {fewestWeights(weight,total)} weights.\n")
    