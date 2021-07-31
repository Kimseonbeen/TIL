function solution(answers) {
    console.log("answers : ",answers); [1, 2, 3, 4, 5]
    var answer = [];
    let one = [1, 2, 3, 4, 5]
    let two = [2, 1, 2, 3, 2, 4, 2, 5]
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let Arr = [0, 0, 0];

    for(let i = 0; i < answers.length; i++) {
        if(answers.length > one.length) {
            one.push(one[i])
        }
        if(answers[i] === one[i]) {
            Arr[0]++
        }
    }

    for(let i = 0; i < answers.length; i++) {
        if(answers.length > two.length) {
            two.push(two[i])
        }
        if(answers[i] === two[i]) {
            Arr[1]++
        }
    }

    for(let i = 0; i < answers.length; i++) {
        if(answers.length > three.length) {
            three.push(three[i])
        }
        if(answers[i] === three[i]) {
            Arr[2]++
        }
    }

    let max2 = Math.max(Arr[0],Arr[1],Arr[2]);

    if(Arr[0] == max2) {
        answer.push(1)
    }
    if(Arr[1] == max2) {
        answer.push(2)
    }
    if(Arr[2] == max2) {
        answer.push(3)
    }

    return answer;
}

let aa  = solution([1, 2, 3, 4, 5])
console.log("aa : ",aa);