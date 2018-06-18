def load_data(file_name='./data.txt'):
    lines = [line for line in open(file_name)]

    # 获取关键字
    col_names = lines[0].strip().split('\t')[1:]
    row_names = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # 获取来源
        row_names.append(p[0])

        # 获取关键字的统计
        data.append([float(x) for x in p[1:]])
    return row_names, col_names, data
