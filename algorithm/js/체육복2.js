function solution(n, lost, reserve) {
    var answer = 0;
    answer = n - lost.length;
    var arr = [];

    for (let i = 0; i < n; i++) {
        arr.push(i + 1)
    }

    for(let k = 0; k < reserve.length; k++) {
        for(let g = 0; g < reserve.length; g++) {
            if(reserve[k] && reserve[k] == lost[g]) {
                reserve.splice(reserve.indexOf(reserve[k]), 1);
                lost.splice(lost.indexOf(lost[g]), 1);
                answer++
            }
        }
    }

    for (let i = 0; i < arr.length; i++) {
        if (reserve.length == 0) {
            return answer
        }
        // 잃어버린 학생 index
        if (arr.includes(lost[i])) {


            if (reserve.includes(lost[i] - 1)) {

                for (let j = 0; j < reserve.length; j++) {
                    if (reserve[j] == lost[i] - 1) {

                        reserve.splice(j, 1);

                        answer++
                    }
                }

            } else if (reserve.includes(lost[i] + 1)) {

                for (let j = 0; j < reserve.length; j++) {
                    if (reserve[j] == lost[i] + 1) {

                        reserve.splice(j, 1);

                        answer++
                    }
                }
            }
        }
    }

    return answer;
}

console.log(solution(10, [1, 7, 8, 9], [2, 3, 4, 5, 6])); // return : 8
console.log(solution(5, [2, 4], [3])); //return : 4
console.log(solution(5, [2, 4], [1, 3, 5])); //return : 5
console.log(solution(5, [2, 4], [3])); // return : 4
console.log(solution(3, [3], [1])); //return : 2
console.log(solution(15, [1, 2, 3, 4, 5, 7, 8, 9, 10], [6, 11, 12])); //return : 8
console.log(solution(10, [1, 2, 3], [2, 3, 8, 9, 10])); //return : 9
console.log(solution(7, [1, 2, 3, 4, 5, 6, 7], [1, 2, 3])); //return : 3
console.log(solution(7, [2, 4, 5, 6, 7], [1, 2, 3, 5, 6, 7])); //return : 7    잃어버렸는데, 여벌 체육복이 있는경우 고려 안함