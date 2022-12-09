function solution(array, commands) {
    const answer = [];
    commands.forEach(command => {
        const splicedArray = array.slice(command[0] - 1, command[1])
        const sortedArray = splicedArray.sort((a, b) => a - b)
        const pickedNum = sortedArray[command[2] - 1]
        answer.push(pickedNum)
    })
    return answer;
}