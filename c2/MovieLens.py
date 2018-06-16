def load_movie_lens(path='./MovieLens'):
    # 读取电影基本信息
    movies = {}
    mf = open(path + '/movies.csv')

    # 去掉头部，第二行才是数据
    mf.readline()
    line = mf.readline()
    while line:
        (mid, title) = line.split(',')[0:2]
        movies[mid] = title
        line = mf.readline()
    mf.close()

    # 读取评分数据
    data = {}
    rf = open(path + '/ratings.csv')
    rf.readline()
    line = rf.readline()
    while line:
        (user, movie_id, rating, ts) = line.split(',')
        data.setdefault(user, {})
        data[user][movies[movie_id]] = float(rating)
        line = rf.readline()
    rf.close()

    return data
