function shiftArr(arr, shiftBy) {
  var temp = 0;
  while (shiftBy > 0) {
    for (var i=arr.length-1; i>0; i--) {
      temp = arr[i];
      arr[i] = arr[i-1];
      arr[i-1] = temp;
    }
    shiftBy--;
  }
  while (shiftBy < 0) {
    for (var i=0; i<arr.length-1; i++) {
      temp = arr[i];
      arr[i] = arr[i+1];
      arr[i+1] = temp;
    }
    shiftBy++;
  }
  return arr;
}
console.log(shiftArr([1, 5, 3, 2, 6], -2));
