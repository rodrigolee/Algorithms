function pushFront(arr, value) {
  arr = reverseArr(arr);
  arr.push(value);
  arr = reverseArr(arr);
  return arr;
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

example = pushFront([1, 4, 5, 2, 3], 19);
console.log(example);
