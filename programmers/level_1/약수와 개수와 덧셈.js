
function solution(left, right) {
    var answer = 0;
    for (let i = left; i <= right; i++) {
        let divisors = 0
        for (let j = 1; j <= i; j++) {
            if (i % j == 0) {
                divisors++;
            }
        }
        if (divisors % 2 == 0) {
            answer += i
        } else {
            answer -= i
        }
    }
    return answer;
}