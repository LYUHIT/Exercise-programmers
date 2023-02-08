function solution(s) {
    var strArr = s.split('')
    var answer = strArr.map((c, i) => {
        let dist = -1
        for (let j = i - 1; j >= 0; j--) {
            if (strArr[j] == c) { dist = i - j; break; }
        }
        return dist
    })
    return answer;
}