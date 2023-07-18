function solution(str1, str2) {
    var answer = 0;
    
    function toSetUpper(str){
        const test = /^[a-zA-Z]*$/
        const strSet = []
        for (let i = 0 ; i < str.length-1 ; i++){
            const temp = str.slice(i,i+2).toUpperCase()
            if (test.test(temp)){
                strSet.push(temp)
            }
        }
        return strSet
    }
    
    function matching(arr1, arr2){
        const minSet=[]
        const maxSet=[]
        
        for (let i = 0 ; i < arr1.length ; i++){
            let same = false
            for (let j = 0 ; j < arr2.length ; j++){
                if (arr1[i] == arr2[j]){
                    minSet.push(arr1[i])
                    maxSet.push(arr1[i]) 
                    arr2.splice(j,1)
                    same = true
                    break;
                }
            }
            if (!same){
                maxSet.push(arr1[i])
            }
        }
        maxSet.push(...arr2)
        return {minSet, maxSet}
        
    }
    
    function calcSame( arr1, arr2 ){
        if (arr1.length == 0 && arr2.length == 0){
            return 65536
        } else if (arr1.length == 0){
            return 0
        } else{
            return Math.floor(arr1.length/arr2.length*65536)
        }
    }
    
    const strs1 = toSetUpper(str1)
    const strs2 = toSetUpper(str2)
    const {minSet, maxSet} = matching(strs1, strs2)
    answer = calcSame(minSet, maxSet)
    
    return answer;
}