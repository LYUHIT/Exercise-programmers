function solution(n) {
    var answer = 0;
    let input = n
    const numThree = []

    for (let i = 3; true; i = 3) {
        numThree.push(n % i)
        n = parseInt(n / i)
        if (n === 0) break;
    }
    const numTen = numThree.reverse();
    numTen.reduce((acc, item, index) => { return answer += item * (3 ** index) }, 0)
    return answer;
}