from itertools import combinations, chain

def sum_to_n(n):
    from operator import sub
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i)) 
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)

scheme = [[1],[1]]
dividedscheme = [[1],[1]]

while True:
    scheme[0][0]=int(scheme[0][0])+1
    for i in range(scheme[0][0]):
        scheme[1][0]=int(i+1)
        for p in sum_to_n(scheme[0][0]):
            for q in sum_to_n(scheme[1][0]):  
                dividedscheme[0]=p
                dividedscheme[1]=q
                print(dividedscheme)

