class decision_node:
    def __init__(self, column_idx=-1, value=None, results=None, true_node=None, false_node=None):
        self.column_idx = column_idx
        self.value = value
        self.results = results
        self.true_node = true_node
        self.false_node = false_node


# 切分为两部分
def divide_set(rows, column, value):
    if isinstance(value, int) or isinstance(value, float):
        split_func = lambda row: row[column] >= value
    else:
        split_func = lambda row: row[column] == value

    set_first = [row for row in rows if split_func(row)]
    set_second = [row for row in rows if not split_func(row)]

    return (set_first, set_second)


# 统计相同行的数量
def unique_counts(rows):
    results = {}
    for row in rows:
        temp_row = row[len(row) - 1]
        if temp_row not in results:
            results[temp_row] = 0
        results[temp_row] += 1
    return results


# 基尼不纯度
def gini_impurity(rows):
    rows_num = len(rows)
    counts = unique_counts(rows)
    impurity = 0

    for count1 in counts:
        p1 = float(counts[count1] / rows_num)
        for count2 in counts:
            if count1 == count2:
                continue
            p2 = float(counts[count2] / rows_num)
            impurity += p1 * p2

    return impurity


# 熵
def entropy(rows):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(rows)
    ent = 0.0
    rows_num = len(rows)
    for row in results.keys():
        p = float(results[row]) / rows_num
        ent -= (p * log2(p))
    return ent


# 建立决策树
def build_trees(rows, score_func=entropy):
    if len(rows) == 0:
        return decision_node()

    current_score = score_func(rows)

    best_gain = 0.0
    best_criteria = None
    best_sets = None
    rows_num = len(rows)

    column_max_idx = len(rows[0]) - 1

    for column_idx in range(0, column_max_idx):
        column_values = {}
        for row in rows:
            column_values[row[column_idx]] = 1

        for value in column_values.keys():
            (set1, set2) = divide_set(rows, column_idx, value)

            # 计算信息增益
            p = len(set1) / rows_num
            gain = current_score - p * score_func(set1) - (1 - p) * score_func(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (column_idx, value)
                best_sets = (set1, set2)

    if best_gain > 0:
        true_node = build_trees(best_sets[0])
        false_node = build_trees(best_sets[1])
        return decision_node(
            column_idx=best_criteria[0], value=best_criteria[1],
            true_node=true_node, false_node=false_node)
    else:
        return decision_node(results=unique_counts(rows))


def print_tree(tree, indent=''):
    if tree.results != None:
        print(indent + str(tree.results))
    else:
        print(indent + 'Idx(' + str(tree.column_idx) + '):', str(tree.value) + '? ')
        print(indent + 'T->')
        print_tree(tree.true_node, indent + '\t')
        print(indent + 'F->')
        print_tree(tree.false_node, indent + '\t')


def classify(observation, tree_node):
    if tree_node.results != None:
        return tree_node.results
    else:
        v = observation[tree_node.column_idx]
        node = None
        if isinstance(v, int) or isinstance(v, float):
            if v >= tree_node.value:
                node = tree_node.true_node
            else:
                node = tree_node.false_node
        else:
            if v == tree_node.value:
                node = tree_node.true_node
            else:
                node = tree_node.false_node
        return classify(observation, node)
