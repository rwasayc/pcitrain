from c5 import data
import random, math


def print_schedule(r, people=data.people, flights=data.flights, destination="LGA"):
    for d in range(int(len(r) / 2)):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin, destination)][int(r[d])]
        ret = flights[(destination, origin)][int(r[d + 1])]
        print('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin,
                                                      out[0], out[1], out[2],
                                                      ret[0], ret[1], ret[2]))


def schedule_cost(r, people=data.people, flights=data.flights, destination="LGA"):
    sum_time = 0
    sum_price = 0
    earliest_leave = 24 * 60  # 最早离开目的地
    latest_arrival = 0  # 最迟到达目的地
    # 计算航班花费及最晚到达时间及最早离开时间
    for idx in range(int(len(r) / 2)):
        people_from = people[idx][1]
        go = flights[(people_from, destination)][int(r[2 * idx])]
        back = flights[(destination, people_from)][int(r[2 * idx + 1])]

        # 计算来回价格
        sum_price += go[2]
        sum_price += back[2]

        # 最迟到达时间
        go_minutes = data.get_minutes(go[1])
        if latest_arrival < go_minutes:
            latest_arrival = go_minutes

        # 最早离开时间
        back_minutes = data.get_minutes(back[0])
        if earliest_leave > back_minutes:
            earliest_leave = back_minutes

    # 计算所有人花费的时间
    for idx in range(int(len(r) / 2)):
        people_from = people[idx][1]
        go = flights[(people_from, destination)][int(r[2 * idx])]
        back = flights[(destination, people_from)][int(r[2 * idx + 1])]

        sum_time += latest_arrival - data.get_minutes(go[1])
        sum_time += data.get_minutes(back[1]) - earliest_leave

    # 多支付一天的费用
    if earliest_leave > latest_arrival:
        sum_price += 50

    return sum_time + sum_price


# 随机搜索
def random_searching(domain, cost_func=schedule_cost):
    best_score = 999999999
    best_result = None
    for try_count in range(2000):
        result = [random.randint(domain[idx][0], domain[idx][1]) for idx in range(len(domain))]
        score = cost_func(result)
        if score < best_score:
            best_score = score
            best_result = result

    return best_score, best_result


# 爬山法
def hill_climbing(domain, cost_func=schedule_cost):
    try_result = [random.randint(domain[idx][0], domain[idx][1]) for idx in range(len(domain))]
    best_score = cost_func(try_result)

    while True:
        neighbors = []
        for idx in range(len(try_result)):
            if try_result[idx] > domain[idx][0]:
                tmp = try_result[:]
                tmp[idx] -= 1
                neighbors.append(tmp)
            if try_result[idx] < domain[idx][1]:
                tmp = try_result[:]
                tmp[idx] += 1
                neighbors.append(tmp)

        unchange = True
        for idx in range(len(neighbors)):
            neighbors_cost = cost_func(neighbors[idx])
            if neighbors_cost < best_score:
                best_score = neighbors_cost
                try_result = neighbors[idx]
                unchange = False

        if unchange:
            break

    return best_score, try_result


# 退火法
def simulated_annealing(domain, cost_func=schedule_cost, T=1000, cool_rate=0.95, step=1):
    try_result = [random.randint(domain[idx][0], domain[idx][1]) for idx in range(len(domain))]
    score = cost_func(try_result)
    while T > 0.1:
        idx = random.randint(0, len(try_result) - 1)
        current_step = random.randint(-step, step)
        temp_result = try_result[:]

        temp_result[idx] += current_step
        if domain[idx][0] > temp_result[idx]:
            temp_result[idx] = domain[idx][0]
        elif domain[idx][1] < temp_result[idx]:
            temp_result[idx] = domain[idx][1]

        temp_score = cost_func(temp_result)
        # print(temp_score, score)
        if temp_score < score or random.random() < pow(math.e, (score - temp_score) / T):
            try_result = temp_result
            score = temp_score

        T *= cool_rate

    return score, try_result


# 遗传算法
def genetic_algorithms(domain, cost_func=schedule_cost, population_size=50, step=1, mutate_rate=0.2, elite_rate=0.2,
                       generation_num=100):
    domain_len = len(domain)

    # 变异
    def mutate(population):
        idx = random.randint(0, domain_len - 1)
        if random.random() < 0.5 and population[idx] > domain[idx][0]:
            return population[0:idx] + [population[idx] - step] + population[idx + 1:]
        elif population[idx] < domain[idx][1]:
            return population[0:idx] + [population[idx] + step] + population[idx + 1:]
        return population[0:idx] + [population[idx] - step] + population[idx + 1:]

    # 交叉
    def crossover(p1, p2):
        idx = random.randint(0, domain_len - 2)
        return p1[0:idx] + p2[idx:]

    # 初始种群
    populations = []
    for idx in range(population_size):
        temp_population = [random.randint(domain[idx][0], domain[idx][1]) for idx in range(len(domain))]
        populations.append(temp_population)

    # 每代留下的个数
    generation_elite_size = int(elite_rate * population_size)

    best_score = 0
    # 开始算法
    for current_generation_no in range(generation_num):
        # 计算及排序分数
        scores = [(cost_func(population), population) for population in populations]
        scores.sort()

        # 选出优胜的种群
        populations = [population for (score, population) in scores[0:generation_elite_size]]
        best_score = scores[0][0]

        while len(populations) < population_size:
            if random.random() < mutate_rate:
                idx = random.randint(0, generation_elite_size - 1)
                populations.append(mutate(populations[idx]))
            else:
                idx1 = random.randint(0, generation_elite_size - 1)
                idx2 = random.randint(0, generation_elite_size - 1)
                populations.append(crossover(populations[idx1], populations[idx2]))

    return best_score, populations[0]
