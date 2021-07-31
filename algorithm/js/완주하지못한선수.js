function solution(participant, completion) {
    participant.sort(); //참가자 배열 정렬
    completion.sort(); //완주자 배열 정렬
    console.log("participant : ",participant);
    console.log("completion : ",completion);
    for(let i in participant){
        if(participant[i] !== completion[i]){
            console.log("true : completion[i] : ",completion[i]);
            //인덱스 0부터 순차적으로 두 배열 비교
            return participant[i];
            //비완주자가 참가자 배열에 나올 경우 출력
        }else {
            console.log("false completion[i] : ",completion[i]);
        }
    }
}

let aa = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]);
console.log("aa :",aa);