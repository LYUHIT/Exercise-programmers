// function solution(s) {
//     var answer = '';
//     const words = s.split("")
//     const A = "A".charCodeAt(0);
//     const Z = "Z".charCodeAt(0);
//     const a = "a".charCodeAt(0);
//     const z = "z".charCodeAt(0);
//     const diff = A - a

//     let next = true;
//     const converted = words.map((c) => {
//         let charC = c.charCodeAt(0)
//         if (next) {
//             if (charC >= a && charC <= z) {
//                 charC += diff;
//             }
//             next = false;
//         }
//         else {
//             if (charC >= A && charC <= Z) {
//                 charC -= diff;
//             }
//         }
//         if (c == " ") next = true;
//         return charC
//     })

//     answer = converted.map(c => String.fromCharCode(c)).join("")
//     return answer;
// }

function solution(s) {
    const words = s.split("")
    let nextUpper = true;
    const converted = words.map(c => {
        if (c == " ") { nextUpper = true; return c }
        else if (nextUpper) { nextUpper = false; return c.toUpperCase(); }
        else { return c.toLowerCase(); }
    })
    return converted.join("")
}