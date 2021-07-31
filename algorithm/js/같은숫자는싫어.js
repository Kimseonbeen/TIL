function solution(arr)
{
    var answer = [];
   
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] !== arr[i+1]) {
            answer.push(arr[i]);
        }
    }
    
    return answer;
}

console.log("solution : ",solution([4,4,4,3,3]));
console.log("solution : ",solution([1,1,3,3,0,1,1]));


function solution2(arr)
{
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] == arr[i+1]) {
            arr.splice(i+1, 1);
            i --
        }
    }
    return arr;
}