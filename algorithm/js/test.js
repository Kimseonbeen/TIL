function solution(numbers) {
    var answer = [2,1,3,4,1];

    let arr = [];
    for(let i = 0; i < answer.length; i++) {

        for(let j = i+1; j < answer.length; j++) {
            let sum = answer[i] + answer[j];
            if(!arr.includes(sum)) {
                arr.push(sum);  
            } 
        }
    }
    console.log("arr : ",arr);
    arr.sort();
    console.log("arr : ",arr);
    return arr;
}

console.log("solution : ",solution());