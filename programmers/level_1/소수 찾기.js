function solution(n) {
    var answer = 0;
    const primeNumber = [];
    for (let i = 2; i <= n; i++) {
        let isPrimeNumber = true
        primeNumber.every(num => {
            if (i % num == 0) {
                isPrimeNumber = false;
                return false
            }
            else {
                return true
            }
        })
        if (isPrimeNumber) {
            primeNumber.push(i)
            answer++;
        }
    }
    return answer;
}

//----------------------------------------

function solution(n) {
    let numbers = []
    for (let a = 2; a <= n; a++) numbers.push(a)

    for (let i = 0; numbers[i] < Math.sqrt(n); i++) {  // 전체배열, numbers[i] 는 소수판별 중인 수 
        numbers = numbers.reduce((acc, item) => {
            if (item % numbers[i] !== 0) {
                acc.push(item)
            }
        }, [numbers[i]])

        answer = numbers.length
        return answer;
    }
}


//----------------------------------------

function solution(n) {
    let numbers = []
    let answer = []

    for (let a = 0; a <= n; a++) numbers.push(a)
    const root = Math.sqrt(n)
    for (let i = 2; i < root; i++) {
        if (numbers[i] !== 1) {
            for (let j = i + 1; j <= n; j++) {
                if (numbers[j] !== 1 && numbers[j] % numbers[i] === 0) {
                    numbers[j] = 1;
                }
            }
        }
    }
    answer = numbers.filter(num => num > 1)
    return answer.length
}

//-----------------------------------
function solution(n) {
    const arr = [];

    // 인덱스 번호가 주어진 숫자 n과 대응하도록 
    // 빈 배열을 만들고 원소는 true 값으로 채워준다.
    // 여기서 true 는 소수라는 의미이다.
    // 배열은 0부터 시작하므로, 주어진 숫자 n에 1을 더해준다.
    for (let i = 0; i < n + 1; i += 1) {
        arr.push(true);
    }

    // 주어진 수의 제곱근까지만 계산해서 불필요한 반복을 최소화한다.
    // arr[i] 가 소수일 경우, 반복문을 진행한다.
    // 맨 처음 시작하는 2는 소수이므로,
    // 2를 제외한 2의 제곱부터, 제곱 값만 체크하여 지워나간다.
    // 제곱근까지 반복한다.
    for (let i = 2; i * i <= n; i += 1) {
        if (arr[i]) {
            for (let j = i * i; j <= n; j += i) {
                arr[j] = false;
            }
        }
    }

    // 0과 1은 소수가 아니므로 false 값으로 바꿔준다.
    arr.splice(0, 2, false, false);

    // 배열에서 true인 값만 걸러내고, true인 값의 개수를 출력한다.
    const result = arr.filter((value) => {
        return value !== false;
    })

    return result.length;
}

//---------------------------------------
function solution(n) {
    let numbers = []
    let answer = []
    const root = Math.sqrt(n)

    // 배열 초기설정
    for (let a = 0; a <= n; a++) numbers.push(true)
    numbers[0] = false
    numbers[1] = false

    // 합성수는 false로 교체
    for (let i = 2; i < root; i++) {
        if (numbers[i]) {
            // 합성수는 기준수의 배수로 찾는다.
            // 시작을 기준수의 제곱으로 한다. (본인 수 제외, 제곱 값 이전의 수는 기준수보다 작은 소수가 시행될 때 이미 걸러짐)
            // 판단해야 할 수는 기준수의 배수이므로, 기준 수를 더해가며 건너 뛴다.
            for (let j = i * i; j <= n; j += i) {
                numbers[j] = false;
            }
        }
    }

    answer = numbers.filter(num => num === true)
    return answer.length
}