function solution(cacheSize, cities) {
    var answer = 0;
    const cashe = []
    const used = []
    let time = 0
    
    const upper = (str)=>{
        return str.toUpperCase()    
    }

    cities.forEach((city, i)=>{
        city = upper(city)
        if (cashe.includes(city)){
            time += 1
            used[cashe.indexOf(city)] = time
        } else {
            time += 5
            if (cashe.length < cacheSize){ 
                cashe.push(city)
                used.push(time)
            }else{
                let least = used.indexOf(Math.min(...used))
                cashe[least] = city
                used[least] = time
            }
        }
    })
    
    return time;
}
