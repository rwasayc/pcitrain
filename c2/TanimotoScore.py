# 谷本系数计算
def ts(data, person_a, person_b):
    i = list(set(data[person_a]).intersection(data[person_b]))
    u = list(set(data[person_a]).union(data[person_b]))
    return len(i) / len(u)
