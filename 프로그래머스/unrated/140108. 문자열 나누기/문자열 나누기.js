function solution(s) {
    var answer = 0;
    const string = s.split('')
    answer = spliceString(string, []).length
    return answer;
}

function spliceString(string, words) {
    let same = 0;
    let diff = 0;

    for (let i = 0; i < string.length; i++) {
        if (string[i] == string[0]) { same++; }
        else { diff++; }

        if (i == string.length - 1) {
            words.push(string.splice(0, same + diff).join(''))
            return words
        }

        if (same == diff) {
            words.push(string.splice(0, same + diff).join(''))
            return spliceString(string, words)
        }
    }
}