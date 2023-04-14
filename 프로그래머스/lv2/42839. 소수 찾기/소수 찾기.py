import math
from itertools import permutations

def solution(numbers):
    answer = 0
    made = set()

    # 숫자 조각의 모든 가능한 순열 생성
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            made.add(num)

    # 소수 판별 함수
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 2
        return True

    # 소수 개수 세기
    for m in made:
        if is_prime(m):
            answer += 1

    return answer
