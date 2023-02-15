function solution(n, lost, reserve) {
    var answer = 0;
    const stu = new Array(n).fill(0)
    lost.forEach(s=> --stu[s-1])
    reserve.forEach(s=> ++stu[s-1])
    
    for(let i =0 ; i<n ; i++){    
        if(stu[i] == -1){
            if (stu[i-1] == 1){
                stu[i]++; 
                stu[i-1]--;
            }
            else if(stu[i+1] == 1){
                stu[i]++; 
                stu[i+1]--;
            }
        }
    }
    answer = stu.filter(s => s>=0).length
    return answer;
}