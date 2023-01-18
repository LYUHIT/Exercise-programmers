function solution(t, p) {
    var answer = 0;
    const pNumber = Number(p)
    const pLength = p.length
    const tLength = t.length
    const parts = []
    
    for (let i = 0 ; i <= tLength-pLength ; i++){
        let part = t.slice(i,i+pLength)
        while(part.length >2 && part[0] == 0){
            part = part.slice(1)
        }
        parts.push(part)
    }
    const answerNums = parts.filter(part => parseInt(part) <= p)
    answer = answerNums.length
    return answer;
}