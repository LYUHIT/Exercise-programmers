def solution(answers):
    answer = []
    points = [0,0,0]
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    
    for i,a in enumerate(answers):
        if s1[i%l1] == a : points[0] +=1
        if s2[i%l2] == a : points[1] +=1
        if s3[i%l3] == a : points[2] +=1
        
    top = max(points)
    for i in range(3):
        if points[i] == top:
            answer.append(i+1)
            
    return answer