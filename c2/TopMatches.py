from c2 import EuclideanDistanceScore, PearsonCorrelationScore


# 获取前N位的近似用户
def top_matches(data, person, n=5, similarity=PearsonCorrelationScore.pcs):
    scores = [(similarity(data, person, check_person), check_person) for check_person in data if person != check_person]
    scores.sort()
    scores.reverse()
    return scores[:n]
