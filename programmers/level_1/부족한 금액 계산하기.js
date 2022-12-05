function solution(price, money, count) {
    let sum = 0
    for (let i = 1; i <= count; i++) {
        sum += price * i
    }
    let answer = money - sum;
    if (answer < 0) {
        return answer * (-1)
    } else {
        return 0
    }
}