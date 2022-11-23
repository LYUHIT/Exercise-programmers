function solution(absolutes, signs) {
    const numbers = []
    for (let i = 0; i < signs.length; i++) {
        signs[i] ? numbers.push(absolutes[i]) : numbers.push(absolutes[i] * -1)
        console.log(numbers[i])
    }
    const answer = numbers.reduce((sum, n) => { return sum + n }, 0)
    return answer
}

function anotherSolution(absolutes, signs) {
    return absolutes.reduce(
        (acc, curr, i) => acc + curr * (signs[i] ? 1 : -1),
        0
    );
}