function removeAt(arr, index) {
  var temp = 0;
  for (var i=arr.length-1; i>=index; i--) {
    temp = arr[index];
    arr[index] = arr[i];
    arr[i] = temp;
  }
  arr.pop();
  return arr;
}

example = removeAt([1, 2, 3, 10, 14, 12], 2);
console.log(example);
