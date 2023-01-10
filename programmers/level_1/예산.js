function solution(d, budget) {
    var answer = 0;
    d.sort((a, b) => { return a - b })
    console.log(`arr : ${d}`)
    d.reduce((acc, item, index) => {
        acc += item
        if (acc <= budget) answer++
        return acc
    }, 0)

    return answer;
}