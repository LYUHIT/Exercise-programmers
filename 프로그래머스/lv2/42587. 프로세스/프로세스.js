function solution(priorities, location) {
    var answer = 0;
    const arr = priorities
    let idx = location
    
    while(true){
        const now = arr.shift()
        idx -= 1
        
        if ( now < Math.max(...arr) ){
            arr.push(now)
            if (idx == -1) idx = arr.length-1
        }else{
            answer++
            if (idx == -1) break
        }
    }
    
    return answer;
}