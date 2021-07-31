function solution(n, lost, reserve) {
    var answer = 0;
    answer = n - lost.length;

    // 1. 여벌의 체육복을 가져온 학생이 체육복을 도난 당한 경우 부터 제외
    // testcase 12번	 
    for (let i = 0; i < lost.length; i++) {
        if (reserve.indexOf(lost[i]) != -1) {      // 도난당한 배열 인덱스 값이 여벌 인덱스 값과 중복일시 체크
            reserve.splice(reserve.indexOf(lost[i]), 1);    // splice 배열 자르기
            lost.splice(i, 1);
            answer++;
            i--;    // 배열을 자르게 되면 배열이 당겨지므로 다시 재 검사

        }
    }

    console.log("lost : ", lost);
    console.log("reserve : ", reserve);

    // 잃어버린 사람 앞이나 뒤에 여벌의 체육복을 가진 사람이 있다면,
    // 체육복을 빌리고, answer을 카운트한다.
    // indexOf : 지정된 요소를 찾으면 인덱스 반환 아닐시 -1 반환
    for (let i = 0; i < lost.length; i++) {
        let forth = reserve.indexOf(lost[i] - 1)   // 앞 체크
        let back = reserve.indexOf(lost[i] + 1)  // 뒤 체크

        // 앞 뒤 비교 시 중복으로 빌려주는것을 제외
        // 빌려준뒤 배열 삭제
        if (forth != -1) {
            reserve.splice(forth, 1);
            answer++;
        }
        if (back != -1) {
            reserve.splice(back, 1);
            answer++;
        }
    }

    return answer;
}

console.log(solution(10, [1, 7, 8, 9], [2, 3, 4, 5, 6])); // return : 8