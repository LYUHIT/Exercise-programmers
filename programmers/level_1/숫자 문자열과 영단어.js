function solution(s) {
    let answer = 0;
    while (String(parseInt(s)).length < s.length) {
        const number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        number.forEach((num, index) => s = s.replace(num, String(index)));
    }
    answer = parseInt(s);
    return answer;
}


//-------------------------------------------
//다른사람의 풀이

function solution2(s) {
    let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    var answer = s;

    for (let i = 0; i < numbers.length; i++) {
        let arr = answer.split(numbers[i]);
        answer = arr.join(i);
    }

    return Number(answer);
}