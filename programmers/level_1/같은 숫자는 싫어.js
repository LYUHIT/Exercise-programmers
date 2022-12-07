function solution(arr) {
    const answer = [];
    arr.forEach((item, index, array) => {
        if (index == 0) { answer.push(item) }
        else if (array[index - 1] !== item) {
            answer.push(item)
        }
    })
    return answer;
}