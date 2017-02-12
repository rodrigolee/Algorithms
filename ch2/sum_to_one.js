function sumToOne(num) {
  var sum = num;
  while (sum > 9) {
    sum = 0;
    while (num > 9) {
      sum = sum + (num % 10);
      num = Math.floor(num / 10);
    }
    sum = sum + num;
    num = sum;
  }
  return sum;
}
var example = sumToOne(318);
console.log(example);
