function solution(babbling) {
    const words = ["aya", "ye", "woo", "ma"]
    let answer = 0;

    babbling.map(babyword => {
        let progress = true;
        let before = "";

        while (progress) {
            for (let i = 0; i < words.length; i++) {
                if (babyword.indexOf(words[i]) == 0) {
                    if (before != words[i]) {
                        before = words[i]
                        babyword = babyword.slice(words[i].length)
                        break;
                    } else {
                        progress = false;
                        break;
                    }
                } else {
                    if (i == words.length - 1) {
                        progress = false;
                        break;
                    }
                }
            }
            if (babyword.length == 0) {
                answer++;
                progress = false;
            }
        }
    })
    return answer;
}