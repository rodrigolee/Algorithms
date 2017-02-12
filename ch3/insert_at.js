function insertAt(arr, index, value) {
  var temp = 0;
  arr.push(value);
  for (var i=index; i<arr.length; i++) {
    temp = arr[i];
    arr[i] = arr[arr.length-1];
    arr[arr.length-1] = temp;
  }
  return arr;
}

example = insertAt([1, 2, 3, 4, 5, 6, 7], 2, 10);
console.log(example);
