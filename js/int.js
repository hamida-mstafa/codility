/* Task: Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
Example:
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017 */
function nextSmaller(n) {
  var nArray = n.toString().split("")
  var length = nArray.length;
  var minimumNum = 1 + Array(length).join('0')
  for(var i=n-1; i >= minimumNum; i--) {
    var newNumArray = i.toString().split('');
    var counter = 0;
    for (var j=0; jnewNumArray.length; j++) {
      if (nArray.indexOf(newNumArray[j]) < 0)
          break;
      counter++
      nArray.splice(nArray.indexOf(newNumArray[j]), 1)
      if (counter === length) {
          return i;
      }
    }
    nArray = n.toString().split("");
  }
  return -1;
}
