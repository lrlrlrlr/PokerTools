from itertools import combinations,permutations,product
from cards.basic import cards, all_comb
import re

num = re.compile(r'[\d+JQKA]')

def is_suited(a,b)->bool:
    return a[-1]==b[-1]

def is_paired(a, b)->bool:
    return num.match(a).group()== num.match(b).group()

def is_trip(comb:tuple)->bool:
    '''
    豹子
    :param comb: ('Ad', 'Ac', 'Ah')
    :return:
    '''
    return all([is_paired(*x) for x in combinations(comb, 2)])


def is_straight_flush(comb:tuple)->bool:
    return is_straight(comb) and is_flush(comb)

def is_straight(comb:tuple)->bool:
    all_straight=['23A','234','345','456','567','678','789','8910','910J','10JQ','JQK',"QKA"]
    nums = ''
    for card in comb:
        nums += num.match(card).group()
    return nums in all_straight and not is_flush(comb)

def is_flush(comb: tuple) -> bool:
    return all(is_suited(*x) for x in combinations(comb,2) )

def is_pair(comb:tuple)->bool:
    return not is_trip(comb) and any([is_paired(*x) for x in combinations(comb, 2)])

def is_high_card(comb:tuple)->bool:
    return not any([is_trip(comb), is_straight_flush(comb),is_flush(comb), is_straight(comb),is_pair(comb)])

# test
print("How many:")
print("All possibilities:", len(all_comb))
print("trip:",len([x for x in all_comb if is_trip(x)]))

print("straight_flush:", len([x for x in all_comb if is_straight_flush(x)]))
print([x for x in all_comb if is_straight_flush(x)])

print("straight:", len([x for x in all_comb if is_straight(x)]))
print("flush:", len([x for x in all_comb if is_flush(x)]))
print("pair:", len([x for x in all_comb if is_pair(x)]))
print("high card:", len([x for x in all_comb if is_high_card(x)]))