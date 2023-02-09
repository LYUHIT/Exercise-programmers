function solution(lottos, win_nums) {
    const answer = [];
    let correct = 0;
    let unknown = 0;
    let high = 0;
    let low = 0;
    const sortedLottos = lottos.sort((a, b) => b - a)
    sortedLottos.forEach(n => {
        if (n > 0) {    // 일치번호 확인
            if (win_nums.includes(n)) {
                correct++;
            }
        }
        else {          // 미지수 개수 파악
            unknown++;
        }
    })
    const myScore = win_nums.length - correct + 1
    low = myScore < 6 ? myScore : 6              // 당첨 최소치
    high = myScore - unknown < 6 ? myScore - unknown : 6   // 당첨 최대치
    answer.push(high, low)
    return answer;
}