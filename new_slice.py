# coding: utf-8

import dis


def add_board():
    board = [['_'] * 3 for i in range(3)]  # 获取一个3*3的数组
    board[1][2] = '*'
    print id(board[0])
    print id(board[1])
    print board

    board = [['_'] * 3] * 3  # 3个['_']指向同一块内存
    board[1][2] = '*'
    print board
    print id(board[0])
    print id(board[1])

    # 等价于:
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    print board


def test():
    print 'test...'
    t = (1, 2, [30, 40])
    print id(t[2])

    # 会出错
    # t[2] += [50, 60]成功是因为t[2]是可变的，也即是元組t存的是list的指针
    # t[2] = t[2]出错是因为元組不可变，但是赋值已经成功了
    try:
        t[2] += [50, 60]
    except Exception as e:
        print e
    print id(t[2])
    print t


if __name__ == '__main__':
    ll = list(range(10))
    ll[1:4] = [20, 50]
    print ll

    del ll[1:4]
    print ll

    print list(range(3)) * 5

    add_board()
    test()
