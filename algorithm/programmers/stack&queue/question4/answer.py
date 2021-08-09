def solution(prices):
    a_list = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            a_list[i] += 1
            if prices[i] > prices[j]:
                break
    return a_list
