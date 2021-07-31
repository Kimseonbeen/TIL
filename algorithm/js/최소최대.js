const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function(line) {
  console.log(line);
  let str = line;
  console.log("str : ",str);
  str = str.split("").reduce((rev, numChar) => numChar + rev, '');
  console.log("str : ",str);
  const eachNumArr = str.split(' ');
  const max = Math.max.apply(null, eachNumArr);
  console.log("str : ",str);
  console.log("eachNumArr : ",eachNumArr);
  console.log("max : ",max);

//   console.log("str1 : ",str1);
//   console.log("str2 : ",str2);

  rl.close();
}).on("close", function() {
  process.exit();
});