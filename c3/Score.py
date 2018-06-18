from math import sqrt


def pcs(v1, v2):
    n = len(v1)

    # 按人计算评分数的和
    sum_a = sum(v1)
    sum_b = sum(v2)

    # 计算平方的和
    sum_a_sq = sum([sqrt(item) for item in v1])
    sum_b_sq = sum([sqrt(item) for item in v2])

    # 计算乘积和
    p_sum = sum([v1[idx] * v2[idx] for idx in range(len(v1))])

    # 计算皮尔逊相关度
    num = p_sum - (sum_a * sum_b / n)

    result = (sum_a_sq - pow(sum_a, 2) / n) * (sum_b_sq - pow(sum_b, 2) / n)

    if result <= 0:
        return 0

    den = sqrt(result)
    if den == 0:
        return 0

    return 1.0 - num / den
