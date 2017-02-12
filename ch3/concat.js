function arrConcat(arr1, arr2) {
  var newArr = [];
  for (var i=0; i<arr1.length; i++) {
    newArr.push(arr1[i]);
  }
  for (var j=0; j<arr2.length; j++) {
    newArr.push(arr2[j]);
  }
  return newArr;
}

example = arrConcat([1, 3, 4], [49, 10]);
console.log(example);
