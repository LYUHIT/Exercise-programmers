function solution(nums) {

    const sumThreeNums = sumThreeNumsInArr(nums)
    const primeNumsArr = judgeNumIsPrime(sumThreeNums)
    return primeNumsArr.length
}

// 3개의 수 더하기
function sumThreeNumsInArr(arr) {
    const arrlen = arr.length
    const sumNumsArr = []
    for (let i = 0; i < arrlen; i++) {
        for (let j = i + 1; j < arrlen; j++) {
            for (let k = j + 1; k < arrlen; k++) {
                sumNumsArr.push(arr[i] + arr[j] + arr[k])
            }
        }
    }
    return sumNumsArr
}

// 배열을 받아서 소수 판단하기
function judgeNumIsPrime(arr) {
    const primeNums = []
    arr.forEach(num => {
        let numIsPrime = true
        for (let i = 2; i < num; i++) {
            if (num % i === 0) {
                numIsPrime = false
                break;
            }
        }
        if (numIsPrime == true) primeNums.push(num)
    })
    return primeNums
}