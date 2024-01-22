/*Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

 pseudocode 
code in javascript*/
function incrementString (input) {
  var reg = /[0-9]/;
  var result = "";
  if(reg.test(input[input.length - 1]) === true){
    input = input.split("");
    for(var i = 0; i < input.length; i++){
        if(parseInt(input[i]) === NaN){
            result += input[i];
        }
        else if(i === input.length - 1){
            result += (parseInt(input[i]) + 1).toString();
        }
        else{
            result += input[i];
        }
    }
    return result;
  }
  else if (reg.test(input[input.length - 1]) === false){
    return input += 1;
  }
}
