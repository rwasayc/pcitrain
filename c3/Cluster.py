from c3 import Score
import random


class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, uuid=None):
        self.vec = vec
        self.left = left
        self.right = right
        self.distance = distance
        self.uuid = uuid


# 分级聚类
# Hierarchical Clustering
def hcluster(rows, dis=Score.pcs):
    cluster = [bicluster(rows[idx], uuid=idx) for idx in range(len(rows))]
    dis_cache = {}
    vec_len = len(cluster[0].vec)
    cur_cluster_uuid = -1

    while len(cluster) > 1:
        key = (0, 1)
        min_dis = dis(cluster[0].vec, cluster[1].vec)

        for fidx in range(len(cluster)):
            for sidx in range(fidx + 1, len(cluster)):
                if (cluster[fidx].uuid, cluster[sidx].uuid) not in dis_cache:
                    dis_cache[(cluster[fidx].uuid, cluster[sidx].uuid)] = dis(cluster[fidx].vec, cluster[sidx].vec)

                cur_dis = dis_cache[(cluster[fidx].uuid, cluster[sidx].uuid)]

                if cur_dis < min_dis:
                    key = (fidx, sidx)
                    min_dis = cur_dis

        merge_vec = [
            (cluster[key[0]].vec[idx] + cluster[key[1]].vec[idx]) / 2.0
            for idx in range(vec_len)]

        new_cluster = bicluster(merge_vec,
                                left=cluster[key[0]], right=cluster[key[1]],
                                distance=min_dis,
                                uuid=cur_cluster_uuid)
        cur_cluster_uuid -= 1
        del cluster[key[1]]
        del cluster[key[0]]
        cluster.append(new_cluster)

    return cluster[0]


def kmeans_cluster(rows, dis=Score.pcs, k=4):
    # 列的个数
    col_num = len(rows[0])
    row_num = len(rows)
    # 计算每一列的值域
    col_ranges = [(min([row[col_idx] for row in rows]), max([row[col_idx] for row in rows]))
                  for col_idx in range(col_num)]
    # 随机k个聚类
    clusters = [
        [
            random.random() * (col_ranges[col_idx][1] - col_ranges[col_idx][0]) + col_ranges[col_idx][0]
            for col_idx in range(col_num)
        ]
        for kidx in range(k)
    ]

    last_best_match = None
    try_time = 0
    while try_time < 100:
        try_time += 1

        best_match = [[] for i in range(k)]
        best_match_k = 0
        for row_idx in range(row_num):
            for kidx in range(1, k):
                temp_dis = dis(rows[row_idx], clusters[kidx])
                if temp_dis < dis(rows[row_idx], clusters[best_match_k]):
                    best_match_k = kidx
            best_match[best_match_k].append(row_idx)

        if last_best_match == best_match:
            break

        last_best_match = best_match

        for kidx in range(k):
            # avgs先用于统计总量，再进行平均计算
            avgs = [0.0] * col_num
            for row_idx in best_match[kidx]:
                for col_idx in range(col_num):
                    avgs[col_idx] += rows[row_idx][col_idx]

            # 对每个数据进行平均计算
            for col_idx in range(col_num):
                bm_num = len(best_match[kidx])
                if bm_num > 0:
                    avgs[col_idx] /= bm_num

            # 用新的均值替换原来的数据
            clusters[kidx] = avgs

    return clusters


# 矩阵转置
def rotate_matrix(data):
    new_data = []
    for r in range(len(data)):
        new_data.append([data[c][r] for c in range(len(data))])
    return new_data
