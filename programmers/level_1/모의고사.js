function solution(answers) {
    const poja1Answer = [1, 2, 3, 4, 5]
    const poja2Answer = [2, 1, 2, 3, 2, 4, 2, 5]
    const poja3Answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    const poja1score = markingSupoja(answers, poja1Answer)
    const poja2score = markingSupoja(answers, poja2Answer)
    const poja3score = markingSupoja(answers, poja3Answer)

    const highScore = Math.max(poja1score, poja2score, poja3score)
    const winners = [poja1score, poja2score, poja3score]
        .reduce((winner, score, index) => {
            if (score == highScore) winner.push(index + 1)
            return winner
        }, [])
    return winners;
}

function markingSupoja(answers, hisAnswer) {
    const hisPattern = hisAnswer.length
    let hisScore = 0
    answers.forEach((n, i) => {
        const thisQuestionHisAnswer = hisAnswer[i % hisPattern]
        if (n == thisQuestionHisAnswer) hisScore++
    })
    return hisScore
}