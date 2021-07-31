function solution(participant, completion) {
    let ret = []
    let hashed = []
    participant.forEach(entry => {
        console.log("entry : ",entry);
        hashed[entry] = hashed[entry] ? hashed[entry] + 1 : 1        
    });
    console.log("hashed : ",hashed);

    completion.forEach(entry => {
        console.log("entry : ",entry);
        hashed[entry] = hashed[entry] - 1
    });
    console.log("hashed : ",hashed);

    for (var key in hashed) {
        if (hashed[key] >= 1) return key
    }
}

let aa = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);
console.log("aa : ",aa);