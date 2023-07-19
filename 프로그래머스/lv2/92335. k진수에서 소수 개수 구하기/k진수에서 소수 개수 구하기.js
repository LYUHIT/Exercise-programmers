function solution(n, k) {
    var answer = -1;

    function changeToK(n,k){
        const result = []
        while(n > 0){
            result.push(n%k)
            n = Math.floor(n / k)
        }
        return result.reverse().join('')
    }
    
    
    function splitZero(n){
        return n.split('0')
    }
    
    
    function isPrime(n){
        if (n == 1 || (n != 2 && n%2 == 0)){
            return false
        }
        for (let i = 3 ; i <= Math.sqrt(n) ; i+=2){
            if (n%i == 0){
                return false
            }
        }
        return true
    }
    
    
    function findPrime(arr){
        let result = 0
        for(let i = 0 ; i < arr.length ; i++){
            if (isPrime(arr[i])){
                result++;
            }
        }
        return result
    }
    
    
    const a = changeToK(n,k)
    const b = splitZero(a)
    const c = findPrime(b)
    answer = c
    
    return answer;
}