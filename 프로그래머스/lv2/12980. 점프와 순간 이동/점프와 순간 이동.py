def solution(n):
    ans = 0
    
    # K칸 점프 : K 소모
    # 현재까지 거리 x2 : 무료
    
    while n > 0:
        ans += n % 2
        n = n // 2
        
    return ans