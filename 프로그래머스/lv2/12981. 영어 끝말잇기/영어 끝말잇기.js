function solution(n, words) {
    var answer = [];
    let wordNum = 0;
    let turn = 1;
    function result (i,n){
        return [ i%n+1, Math.floor(i/n)+1 ]
    }
    for (let i = 1 ; i < words.length ; i++){
        if ( words[i-1][words[i-1].length-1] != words[i][0] ){
            return result(i,n)
        }
        for (let j = 0 ; j < i ; j++){
            if (words[j] == words[i]){
                return result(i,n)
            }
        }
    }
    return [0,0];
}