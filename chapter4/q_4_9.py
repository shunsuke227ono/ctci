# coding: UTF-8

# 木を上る方向に考えることでlog(n)の計算量で済む
# もし下る方向に全て考えるとなると、計算量はnになる

def find_sum(node, given_sum, path=None, depth=0):
    if node is None:
        return
    if path is None:
        path = []

    # 参照渡しなのですでに配列長さ揃っている可能性もある
    # その場合は今回の箇所を上書きすれば問題ない
    if len(path) > depth:
        path[depth] = node.value
    else:
        path.append(node.value)

    temp = 0
    for i in range(depth, -1, -1):
        temp += path[i]
        if temp == given_sum:
            printPath(path, i, depth)

    find_sum(node.left, given_sum, path, depth+1)
    find_sum(node.right, given_sum, path, depth+1)

def printPath(path, start, end):
    for i in range(start, end + 1):
        print path[i]
