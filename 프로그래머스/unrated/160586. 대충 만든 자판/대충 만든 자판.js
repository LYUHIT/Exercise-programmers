function solution(keymap, targets) {
    // 가장 긴 키의 길이
    var answer = [];
    const keymax = keymap.reduce((acc, i) => {
        if (acc < i.length) acc = i.length
        return acc
    }, 0)

    // 가장 적게 누르는 수 계산하기
    targets.forEach(target => {
        let count = []
        for (let t = 0; t < target.length; t++) {
            count.push(howManyClick(keymap, keymax, target[t]))
        }
        if (count.includes(-1)){answer.push(-1)}
        else{answer.push(count.reduce((acc,i)=>{return acc+i},0))}
    
    })
    return answer;
}

// 어떤 글자가 주어진 키패드에서 최소 몇번 눌러야 하는지
function howManyClick(keymap, n, targetChar) {
    for (let i = 0; i < n; i++) {
        for (let k = 0; k < keymap.length; k++) {
            if (keymap[k][i] == targetChar) { return i + 1 }
        }
    }
    return -1
}