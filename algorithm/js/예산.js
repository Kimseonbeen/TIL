function solution(d, budget) {
    var count = 0;
    var sum = 0;
    
    d.sort((a, b) => { return a - b; }); // 문자 정렬, 아스키코드 순서로 정렬하기 때문에 순서로 정렬되지 않음.
    
    for(var i=0; i < d.length; i++) {
        count++;
        sum += d[i];
        if(sum > budget) {
            count--;
            break;
        }
    }
    return count;
}

console.log("solution : ",solution([1,3,2,5,4], 9));
console.log("solution : ",solution([2,2,3,3], 10));


// sort
// function compare(a, b) {
//     if (a가 b보다 작다면) {
//       return -1;
//     }
//     if (a가 b보다 크다면) {
//       return 1;
//     }
//     return 0; // a=b라면
//   }