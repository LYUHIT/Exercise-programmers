function solution(s) {
    let answer = true;
    if (!((s.length == 4) || (s.length == 6))) { answer = false }
    const str = s.split("")
    str.forEach((a) => {
        if (a < '0' || a > '9') { answer = false; }
    })
    return answer;
}