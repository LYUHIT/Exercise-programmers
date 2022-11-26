function solution(a, b) {
    const answer = a.reduce((acc, num, index) => {
        return acc + num * b[index]
    }, 0)
    return answer;
}