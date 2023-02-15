function solution(participant, completion) {
    var answer = '';
    const hash = new Map()
    
    for (let i = 0 ; i < participant.length ; i++){
        const a = participant[i];
        const b = completion[i];
        hash.set(a, (hash.get(a)||0) + 1)
        hash.set(b, (hash.get(b)||0) - 1)
    }
    
    for ([k,v] of hash){
        if (v > 0) answer = k
    }
    return answer;
}