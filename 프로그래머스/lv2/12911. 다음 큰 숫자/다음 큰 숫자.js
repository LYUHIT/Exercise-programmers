function solution(n) {
    var answer = 0;
    const nOne = countOne(n)
    
    while( !answer ){
        n++;
        if (countOne(n) == nOne) answer = n;
    }
    
    function countOne(num){
        let result = 0;
        num.toString(2).split("").forEach(i=>{if(i=='1') result++;})
        return result;
    }
    
    return answer;
}