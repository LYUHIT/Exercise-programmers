function solution(sizes) {
    var answer = 0;
    let wideOfWallet = 0;
    let heightOfWallet = 0;

    const resize = sizes.map(i => {
        return i.sort((a, b) => a - b)
    })

    resize.forEach((i) => {
        if (i[0] > wideOfWallet) {
            wideOfWallet = i[0]
        }
        if (i[1] > heightOfWallet) {
            heightOfWallet = i[1]
        }
    })

    answer = wideOfWallet * heightOfWallet
    return answer;
}

//--------------------
// 다른 사람의 풀이
function solution2(sizes) {
    const rotated = sizes.map(([w, h]) => w < h ? [h, w] : [w, h]);

    let maxSize = [0, 0];
    rotated.forEach(([w, h]) => {
        if (w > maxSize[0]) maxSize[0] = w;
        if (h > maxSize[1]) maxSize[1] = h;
    })
    return maxSize[0] * maxSize[1];
}