function solution(progresses, speeds) {
    var answer = [];
    let lastDeploy = 0
    let nowDeploy = 0
    
    while (nowDeploy < progresses.length){
        progresses = progresses.map( (a,i)=> a + speeds[i] )
        if (progresses[lastDeploy] >= 100){
            while (nowDeploy < progresses.length && progresses[nowDeploy] >= 100){
                nowDeploy++
            }
            answer.push(nowDeploy-lastDeploy)
            lastDeploy = nowDeploy
        }
    }
    return answer;
}