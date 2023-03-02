function solution(ingredient) {
    var answer = 0;
    let made = 0;
    let nextpoint = 0;
        
    while(nextpoint <= ingredient.length-4){
        for (let i = nextpoint ; i <= ingredient.length-4 ; i++){
            if (ingredient[i] == 1 
                && ingredient[i+1] == 2 
                && ingredient[i+2] == 3 
                && ingredient[i+3] == 1){
                made++;
                ingredient.splice(i,4)
                nextpoint = i-3 < 0 ? 0 : i-3
                break;
            }else{
                nextpoint = i+1
            }
        }       
    }
    answer = made;
    return answer;
}
