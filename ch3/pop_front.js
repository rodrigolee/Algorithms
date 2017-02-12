function popFront(arr) {
  arr = reverseArr(arr);
  arr.pop();
  return reverseArr(arr);
}

function reverseArr(arr) {
  var temp = 0;
  for (var i=0; i<arr.length/2; i++) {
    temp = arr[i];
    arr[i] = arr[arr.length-1-i];
    arr[arr.length-1-i] = temp;
  }
  return arr;
}

example = popFront([1, 5, 3, 2, 10]);
console.log(example);
