function solution(s) {
    var answer = '';
    let arr = []
    for(let i = 0; i < s.length; i++) {
        arr.push(s[i])
    }
    arr.sort(); // 정렬
    arr.reverse();  // 배열 뒤집기
    console.log("arr : ", arr);
    for(let j = 0; j < arr.length; j++) {
        answer += arr[j]
    }
    return answer;
}

console.log("solution : ",solution("Zbcdefg"));
