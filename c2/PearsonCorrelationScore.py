from math import sqrt


def pcs(data, person_a, person_b):
    # 获取都评价过的电影
    same_data = {}
    for item in data[person_a]:
        if item in data[person_b]:
            same_data[item] = 1

    n = len(same_data)
    if n == 0:
        return 0

    # 按人计算评分数的和
    sum_a = sum([data[person_a][item] for item in same_data])
    sum_b = sum([data[person_b][item] for item in same_data])

    # 按人计算评分平方的和
    sum_a_sq = sum([sqrt(data[person_a][item]) for item in same_data])
    sum_b_sq = sum([sqrt(data[person_b][item]) for item in same_data])

    # 计算同一个电影的a、b用户评分成绩和
    p_sum = sum([data[person_a][item] * data[person_b][item] for item in same_data])

    # 计算皮尔逊相关度
    num = p_sum - (sum_a * sum_b / n)

    result = (sum_a_sq - pow(sum_a, 2) / n) * (sum_b_sq - pow(sum_b, 2) / n)
    if result <= 0:
        return 0

    den = sqrt(result)
    if den == 0:
        return 0

    return num / den
