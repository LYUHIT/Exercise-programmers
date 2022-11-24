function solution(n) {
    const arr = [];
    for (let i = 1; i <= n; i++) {
        i % 2 == 0 ? arr.push("박") : arr.push("수")
    }
    const answer = arr.join("")
    return answer;
}