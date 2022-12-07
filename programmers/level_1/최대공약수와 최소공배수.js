function solution(n, m) {

    function findDivs(n) {
        const divs = [];
        for (let i = 1; i <= n; i++) {
            if (n % i == 0) { divs.push(i) }
        }
        return divs
    }

    function findDivAndMul(arr1, arr2) {

        const maxDiv = arr1.filter((i) => { return arr2.indexOf(i) !== -1 }).sort((a, b) => a - b).pop()
        const minMul = n * m / maxDiv
        return [maxDiv, minMul]
    }

    return findDivAndMul(findDivs(n), findDivs(m));
}


//--------------------------------
// 다른 사람의 풀이 

function gcdlcm(a, b) {
    var r;
    for (var ab = a * b; r = a % b; a = b, b = r) { }
    return [b, ab / b];
}