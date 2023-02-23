function solution(new_id) {
    var answer = '';
    const id = new_id.toLowerCase().split("")
    const allowedCharId = allowChar(id)
    const removedDoubblePoint = rmDoubblePoint(allowedCharId)
    const notPointInEnd = rmPointInEnd(removedDoubblePoint)
    const cuttedId = cuttingIdBy15(notPointInEnd)
    const finalId = makeIdUpto3(cuttedId)
    answer = finalId.join("")
    return answer;
}

//------------------------------------------------------

function allowChar(id) {
    return id.filter(char => {
        const c = char.charCodeAt(0)
        if ("a".charCodeAt(0) <= c && c <= "z".charCodeAt(0)) return true
        if ("0".charCodeAt(0) <= c && c <= "9".charCodeAt(0)) return true
        if (char == "-" || char == "_" || char == ".") return true
        return false
    })
}

function rmDoubblePoint(arr) {
    return arr.reduce((acc, c, i, arr) => {
        if (c == "." && arr[i + 1] == ".") return acc;
        acc.push(c)
        return acc
    }, [])
}

function rmPointInEnd(arr) {
    if (arr[0] == ".") {
        arr.shift()
        return rmPointInEnd(arr)
    }
    if (arr[arr.length - 1] == ".") {
        arr.pop()
        return rmPointInEnd(arr)
    }
    if (arr.length == 0) {
        arr.push("a")
    }
    return arr
}

function cuttingIdBy15(arr) {
    const cutted = arr.slice(0, 15)
    return rmPointInEnd(cutted)
}

function makeIdUpto3(arr) {
    if (arr.length < 3) {
        arr.push(arr[arr.length - 1])
        return makeIdUpto3(arr)
    }
    return arr
}
