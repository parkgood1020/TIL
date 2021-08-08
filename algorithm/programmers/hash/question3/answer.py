def solution(clothes):
    d = {}
    for c in clothes:
        if c[1] in d:
            d[c[1]] += 1
        else:
            d[c[1]] = 1
    cnt = 1
    for v in d.values():
        cnt *= (v+1)
    return cnt - 1
