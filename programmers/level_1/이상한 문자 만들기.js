function solution(s) {
    const answer = [];
    let isUpper = true
    const input = s.split("")

    input.forEach((word, index, arr) => {
        if (word === " ") {
            isUpper = true
            answer.push(" ")
        } else {
            if (isUpper) {
                answer.push(word.toUpperCase())
            } else {
                answer.push(word.toLowerCase())
            }
            isUpper ? isUpper = false : isUpper = true
        }

    })
    const answerStr = answer.join("")
    return answerStr;
}