function solution(number, limit, power) {
    var answer = 0;
    var powers = [];

    for (let n = 1; n <= number; n++) {
        let p = 0;
        for (let i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (i == n / i) p++;
                else p = p + 2;
            }
        }
        powers.push(p)
    }

    answer = powers.reduce((acc, po) => {
        if (po > limit) return acc + power
        else return acc + po
    }, 0)

    return answer;
}