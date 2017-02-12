function reverse(arr) {
  var temp = 0;
  for (var i=0; i<arr.length/2; i++) {
    temp = arr[i];
    arr[i] = arr[arr.length-1-i];
    arr[arr.length-1-i] = temp;
  }
  return arr;
}

example = reverse([1, 2, 3, 4, 5, 6, 7]);
console.log(example);
