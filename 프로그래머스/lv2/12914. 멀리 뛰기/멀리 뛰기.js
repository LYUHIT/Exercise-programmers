function solution(n) {
    var answer = 0;
    
    const dp =[]
    dp.push(0,1,2)
    
    while (dp.length < n+1){
        let i = dp.length
        dp.push((dp[i-1]+dp[i-2])%1234567)
    }
    answer = dp[n]
    return answer
}


