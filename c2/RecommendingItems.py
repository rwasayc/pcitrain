from c2 import PearsonCorrelationScore


# 获取推荐的物品本身
def get_recommending_items(data, person, similarity=PearsonCorrelationScore.pcs):
    total = {}
    sums = {}
    for check_person in data:
        if check_person == person:
            continue

        sim = similarity(data, person, check_person)
        if sim <= 0:
            continue

        for item in data[check_person]:
            if item in data[person] and data[person][item] > 0:
                continue

            total.setdefault(item, 0)
            total[item] += sim * data[check_person][item]

            sums.setdefault(item, 0)
            sums[item] += sim

    rankings = [(score / sums[item], item) for item, score in total.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
