from c3 import Score


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


def ahcluster(rows, distance=Score.pcs):
    distances = {}
    currentclustid = -1

    # Clusters are initially just the rows
    clust = [bicluster(rows[i], uuid=i) for i in range(len(rows))]

    while len(clust) > 1:
        lowestpair = (0, 1)
        closest = distance(clust[0].vec, clust[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(clust)):
            for j in range(i + 1, len(clust)):
                # distances is the cache of distance calculations
                if (clust[i].uuid, clust[j].uuid) not in distances:
                    distances[(clust[i].uuid, clust[j].uuid)] = distance(clust[i].vec, clust[j].vec)

                d = distances[(clust[i].uuid, clust[j].uuid)]

                if d < closest:
                    closest = d
                    lowestpair = (i, j)

        # calculate the average of the two clusters
        mergevec = [
            (clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i]) / 2.0
            for i in range(len(clust[0].vec))]

        # create the new cluster
        newcluster = bicluster(mergevec, left=clust[lowestpair[0]],
                               right=clust[lowestpair[1]],
                               distance=closest, uuid=currentclustid)

        # cluster ids that weren't in the original set are negative
        currentclustid -= 1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]


# def kmeans_cluster(row, dis=Score.pcs, k=4):


# 矩阵转置
def rotate_matrix(data):
    new_data = []
    for r in range(len(data)):
        new_data.append([data[c][r] for c in range(len(data))])
    return new_data
