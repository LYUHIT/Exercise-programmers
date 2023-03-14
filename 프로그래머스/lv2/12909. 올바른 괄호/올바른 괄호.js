function solution(s){
    var answer = true;
    let bracket = 0;
    const length = s.length
    
    for( let i = 0 ; i < length ; i++ ){
        if (s[i] == '(') bracket++;
        else bracket--;
        if(bracket < 0){
            answer = false;
            break;
        }
        if(bracket > length-i){
            answer = false;
            break;
        }
    }
    if(bracket != 0){
        answer = false;
    }

    return answer;
}