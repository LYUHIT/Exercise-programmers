function solution(brown, yellow) {
    var answer = [];
    const sideBrown = brown - 4;

    for (let i = 1 ; i <= Math.sqrt(yellow) ; i++){
        if(yellow % i == 0){
            const y1 = i;
            const y2 = Math.floor(yellow / i);
            if( sideBrown == (y1+y2)*2 ){
                return [y2+2 , y1+2]
            }
        }
    }
}