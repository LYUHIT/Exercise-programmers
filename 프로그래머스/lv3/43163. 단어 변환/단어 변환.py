import re

def solution(begin, target, words):
    answer = 0
    dic = {}
    queue = []

    if target not in words :
        return 0
    
    dic[begin] = 0
    queue.append(begin)
    
    while queue :
        now = queue.pop(0)
        for i in range(len(now)):
            for j in range(len(words)):
                match = re.search(now[:i]+r'[a-z]'+now[i+1:], words[j])
                if match is not None:
                    if dic.get(words[j]) is None:
                        queue.append(words[j])
                        dic[words[j]] = dic[now]+1

    answer = dic.get(target,0)

    return answer
