import operator
import random


def simple():
    dic_list = []
    for num in range(10):
        new_dic = {'id': num, 'edad': random.randint(1, 100)}
        dic_list.append(new_dic)
    return dic_list


def output():
    dic_list = simple()
    sorted_list = sorted(dic_list, key=operator.itemgetter('edad'))
    print(sorted_list[0]['id'])
    print(sorted_list[-1]['id'])
    return sorted_list

