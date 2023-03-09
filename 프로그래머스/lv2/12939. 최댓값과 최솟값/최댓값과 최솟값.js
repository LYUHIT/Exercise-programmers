function solution(s) {
    let answer = [];
    const numbers = s.split(" ");
    answer.push(Math.min(...numbers))
    answer.push(Math.max(...numbers))
    answer = answer.join(" ")
    return answer;
}