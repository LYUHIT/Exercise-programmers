function solution(k, m, score) {
    var answer = 0;
    const sortedApple = score.sort((a, b) => b - a)
    const boxScore = [];
    for (let i = 1; m * i <= score.length; i++) {
        boxScore.push(sortedApple[m * i - 1] * m);
    }
    answer = (boxScore.reduce((sum, score) => sum + score, 0))
    return answer;
}