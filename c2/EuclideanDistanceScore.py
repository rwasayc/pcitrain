

from math import sqrt


# 原书中sim_distance函数
# 欧几里得距离计算
def eds(data, person_a, person_b):
    # 获取用户A和B都评价过的电影
    sum_same_data = [
        pow(data[person_a][item] - data[person_b][item], 2)
        for item in data[person_a] if item in data[person_b]
    ]

    if len(sum_same_data) == 0:
        return 0
    else:
        return 1 / (1 + sqrt(sum(sum_same_data)))


