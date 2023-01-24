function solution(N, stages) {
    
    // 스테이지 별 유저 수 확인
    const userOfStage = new Array(N + 2).fill(0)
    const failureRateOfStage = new Array(N + 2).fill(0)
    stages.forEach(i => userOfStage[i]++)

    // 스테이지 별 실패율 확인
    let users = 0;
    for (let n = N + 1; n > 0; n--) {
        users = users + userOfStage[n]
        if (users == 0) { failureRateOfStage[n] = 0 }
        else { failureRateOfStage[n] = userOfStage[n] / users }
    }

    // 스테이지 번호와 실패율을 묶음
    const failureMap = failureRateOfStage
        .map((rate, index) => { return { "index": index, "rate": rate } })
    
    // 필요없는 스테이지 제거 (스테이지 0, 전체스테이지 클리어)
    failureMap.pop();
    failureMap.shift();

    // 실패율 순 스테이지 나열
    const rankOfFailure = failureMap.sort((a, b) => {
        if (a.rate == b.rate) { return a.index - b.index; }
        else { return b.rate - a.rate }
    });
    const answer = rankOfFailure.map(i => { return i.index })
    return answer;
}

