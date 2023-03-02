function solution(ingredient) {
    var answer = 0;
    let made = 0;

    for (let i = 0 ; i <= ingredient.length - 4; i++) {
        if (ingredient[i] == 1
            && ingredient[i + 1] == 2
            && ingredient[i + 2] == 3
            && ingredient[i + 3] == 1) {
                made++;
                ingredient.splice(i, 4)
                i -= 4;
        }
    }
    answer = made;
    return answer;
}
