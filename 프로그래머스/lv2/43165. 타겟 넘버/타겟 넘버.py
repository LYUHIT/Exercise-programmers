def solution(numbers, target):
    def dfs( n, sums, numbers, target ):
        if n == len(numbers):
            if sums == target:
                return 1
            else : return 0
        
        plus = dfs( n+1, sums+numbers[n], numbers, target )
        minus = dfs( n+1, sums-numbers[n], numbers, target )
        return plus+minus

    answer = dfs(0, 0, numbers, target)
    return answer