const solution = (strings, n) => {
  console.log("strings : ",strings);


// 이 함수가 리턴하는 값이 0보다 작을 경우,  a가 b보다 앞에 오도록 정렬하고,
// 이 함수가 리턴하는 값이 0보다 클 경우, b가 a보다 앞에 오도록 정렬합니다.
// 만약 0을 리턴하면, a와 b의 순서를 변경하지 않는다.
strings.sort((a, b) => {
  console.log("a : ",a);
  console.log("b : ",b);
  if(a[n] > b[n]) return 1;
  if(a[n] < b[n]) return -1;
  if(a[n] === b[n]){
      if(a>b) return 1;
      if(a<b) return -1;
      return 0;
  }
  console.log("strings : ",strings);
});

return strings
}

console.log("solution : ", solution(["sun", "bed", "car"], 1));