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