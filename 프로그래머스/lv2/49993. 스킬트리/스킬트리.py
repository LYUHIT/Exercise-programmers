def solution(skill, skill_trees):
    answer = 0
    skills = list(skill)
    
    def inthere(i):
        return i in skill
    
    for tree in skill_trees:
        ltree = list(tree)
        newtree = list(filter(inthere,ltree))
        
        for n in newtree:
            if newtree.index(n) != skills.index(n):
                possible = False
                break
                
        else: 
            answer += 1
                
    return answer