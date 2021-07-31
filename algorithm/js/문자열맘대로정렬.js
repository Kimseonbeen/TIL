function solution(strings, n) {
    strings.sort();

    // for(let i = 0; i < strings.length; i++) {
    //     nArr.push(strings[i][n]);
    // }

    // 이중 포문으로 다 돌려
    for (let i = 0; i < strings.length - 1; i++) {
        for (let j = i + 1; j < strings.length; j++) {
            // n 인덱스 확인후 클때마다 배열 위치 바꿔
            if (strings[i][n] > strings[j][n]) {
                [strings[i], strings[j]] = [strings[j], strings[i]];

            // n 인덱스 같을경우
            } if (strings[i][n] === strings[j][n]) {
                if (strings[i] > strings[j]) {
                    [strings[i], strings[j]] = [strings[j], strings[i]];
                }
            }
        }
    }
    return strings;
}


console.log("solution : ", solution(["sun", "bed", "car"], 1));