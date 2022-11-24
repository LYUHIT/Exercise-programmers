function solution(s) {
    const len = s.length
    const center = (len - 1) / 2
    const answer = (len % 2 == 0) ? s.substring(center, center + 2) : s.substring(center, center + 1)
    return answer
}

//substring() 에 소수점이 들어갈 경우, 자동으로 floor 처리 되는 듯 하다.