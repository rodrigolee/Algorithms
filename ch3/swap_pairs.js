function swapPairs(arr) {
  var temp;
  for (var i=0; i<arr.length-1; i+=2) {
    temp = arr[i];
    arr[i] = arr[i+1];
    arr[i+1] = temp;
  }
  return arr;
}

example = swapPairs([1, 2, 'test', 3, 4, 5, 'hello']);
console.log(example);
