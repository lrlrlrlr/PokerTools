from itertools import combinations,permutations,product
c = ['d','c','h','s']
n = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

cards = [''.join(x) for x in list(product(n,c))]
all_comb = list(combinations(cards,3))