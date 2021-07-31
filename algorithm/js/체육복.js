function solution(n, lost, reserve) {
    var answer = 0;
    answer = n - lost.length;
    console.log("answer : ", answer);
    var arr = [];
    console.log("n : ", n);
    console.log("lost : ", lost);
    console.log("reserve : ", reserve);
    for (let i = 0; i < n; i++) {
        arr.push(i + 1)
    }
    console.log("arr : ", arr);

    console.log("reserve.length : ",reserve.length);

    // 여벌 체육복 있는 학생 and 도난 당한 학생
    for(let k = 0; k <= reserve.length; k++) {
        console.log("true : ",reserve[k]);
        for(let g = 0; g <= lost.length; g++) {
            console.log("lost[g]",lost[g]);
            if(reserve[k] && reserve[k] == lost[g]) {
                console.log("reserve[k] : ", reserve[k]);
                reserve.splice(reserve.indexOf(reserve[k]), 1);         // 지울시 배열이 당겨져서 오류남
                lost.splice(lost.indexOf(lost[g]), 1);
                console.log("true2 : ",reserve[k]);
                answer++
            }
        }
    }

    console.log("reserve@@ : ",reserve);
    console.log("lost@@ : ",lost);
    console.log("arr@@ : ",arr);



    // 여벌 체육복이 없는 경우
    for (let i = 0; i < arr.length; i++) {
        if (reserve.length == 0) {
            return answer
        }
        // 잃어버린 학생 index
        if (arr.includes(lost[i])) {
            console.log("lost[i]!!!! : ", lost[i]); // 포문안 첫 번째 잃어버린 학생
            if (reserve.includes(lost[i] - 1)) {    // 잃어버린 학생 앞 인덱스
                console.log("reserve.includes(lost[i]-1 : ");
                for (let j = 0; j < reserve.length; j++) {
                    if (reserve[j] == lost[i] - 1) {        // 포문 돌려서 여벌 체육복 빌려 줄 수있는 사람 확인
                        console.log("reserve[j] : ", reserve[j]);
                        reserve.splice(j, 1);               // 확인 되면  reserve 인덱스에서 삭제
                        console.log("reserve : ", reserve);
                        answer++
                    }
                }
                console.log("answer : ", answer);
                console.log("reserve : ", reserve);
                console.log("lost[i]@ : ", lost[i]);
            } else if (reserve.includes(lost[i] + 1)) { // 잃어버린 학생 뒤 인덱스
                console.log("reserve.includes(lost[i] + 1)");
                for (let j = 0; j < reserve.length; j++) {
                    if (reserve[j] == lost[i] + 1) {
                        console.log("reserve[j] : ", reserve[j]);
                        reserve.splice(j, 1);
                        console.log("reserve : ", reserve);
                        answer++
                    }
                }
            }
        }
    }
    console.log("answer : ",answer);
    return answer;
}

console.log(solution(10, [1, 2, 3], [2, 3, 8, 9, 10])); //return : 9


// 테스트 케이스 12 : 먼저 여벌 체육복 갖고 있고, 잃어버린 사람 부터 찾아야함