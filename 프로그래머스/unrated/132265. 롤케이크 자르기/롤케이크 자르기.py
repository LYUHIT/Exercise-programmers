def solution(topping):
    answer = 0
    idx = 0
    left = {}
    right = {}
    
    def addcake(where,topping):
        if where.get(topping) is None : where[topping] = 1
        else : where[topping] += 1
    def removecake(where, topping):
        if where.get(topping) > 1 : where[topping] -= 1
        else : del(where[topping])
    
    for top in topping:
        addcake(right,top)

    while len(left) <= len(right) :
        top = topping[idx]
        removecake(right,top)
        addcake(left,top)
        if len(right) == len(left):
            answer += 1
        idx += 1

    return answer