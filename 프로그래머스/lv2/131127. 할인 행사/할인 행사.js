function solution(want, number, discount) {
    var answer = 0;
    const cart = {}
    const l = want.length
    
    function canJoin(cart){
    let plus = true
    for (let m in cart){
        if (cart[m] > 0){
            plus = false
            break
        }
    }
    if(plus){
        answer += 1
    }
}
    
    // 초기세팅
    for (let i = 0 ; i < l ; i++){  
        cart[want[i]] = number[i]
    }
    
    for (let j = 0 ; j < 10 ; j++){  
        if (want.includes(discount[j])){
             cart[discount[j]]-=1   
        }
    }
    
    canJoin(cart)
    
    // 한칸씩 이동하며 체크
    for (let k = 0 ; k < discount.length - 10 ; k++){
        if (want.includes(discount[k])){
            cart[discount[k]]+=1
        }
        if (want.includes(discount[k+10])){
            cart[discount[k+10]]-=1
        }
        canJoin(cart)
    }
    return answer;
}

