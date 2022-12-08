function solution(s, n) {
    var answer = '';
    const codes = []
    for (i = 0; i < s.length; i++) {
        let code = s.charCodeAt(i)
        if (code >= 65 && code <= 90) {
            code += n
            if (code > 90) code -= 26
        } else if (code >= 97 && code <= 122) {
            code += n
            if (code > 122) code -= 26
        }
        codes.push(code)
    }
    answer = codes.map((item) => String.fromCharCode(item)).join("")
    return answer;
}