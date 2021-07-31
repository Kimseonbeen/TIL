function solution(s) {
    var answer = '';

    //let mid = Math.length / 2;
    let mid = Math.ceil(s.length / 2);
    console.log("mid : ", mid);

    if(s.length % 2 == 0) {
        answer = s[mid - 1] + s[mid];
    } else {
        answer = s[mid - 1];
    }

    return answer;
}

console.log("solution : ",solution('abcd'));
console.log("solution : ",solution('abcde'));
console.log("solution : ",solution('abcdefg'));
console.log(Math.ceil(2.3));