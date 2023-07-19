function solution(n, t, m, p) {
    var answer = [];
    const numbers = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    let order = 0
    let number = 0
    const l = n-1
    
    while(answer.length < t){
        let now = number
        const nows = []
        if (now == 0) nows.push(0)
        while (now > 0){
            nows.push(now%n)
            now = Math.floor(now/n)
        }
        nows.reverse()

        const Nnows = nows.map((a)=>numbers[a])
        const nowStr = Nnows.join('')
        const nowStrs = nowStr.split('')
        
        nowStrs.forEach((a)=>{
            if (order%m == p-1){
                answer.push(a)
            }
            order++
        })
        number++
    }
    answer = answer.slice(0,t)
    answer = answer.join('')
    return answer;
}