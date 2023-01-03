function solution(a, b) {
    const dayOfTheWeek = {
        1: "FRI",
        2: "SAT",
        3: "SUN",
        4: "MON",
        5: "TUE",
        6: "WED",
        7: "THU",
    }
    let days = b
    let answer = '';

    for (let i = 1; i < a; i++) {
        switch (i) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                days += 31
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                days += 30
                break;
            case 2:
                days += 29
                break;
        }
    }
    const dayOfTheWeekNumber = days % 7;
    answer = dayOfTheWeek[dayOfTheWeekNumber]
    return answer;
}

//----------------------------------------------------------

function solution(a, b) {
    const dayOfTheWeek = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    const day31Months = [1, 3, 5, 7, 8, 10, 12]
    const day30Months = [4, 6, 9, 11]

    let days = b
    let answer = '';

    for (let i = 1; i < a; i++) {
        if (day31Months.includes(i)) days += 31
        else if (day30Months.includes(i)) days += 30
        else days += 29
    }

    const dayOfTheWeekNumber = days % 7;
    answer = dayOfTheWeek[dayOfTheWeekNumber]
    return answer;
}