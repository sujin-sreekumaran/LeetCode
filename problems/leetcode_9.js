var isPalindrome = function (x) {
  const reversed = x.toString().split("").reverse().join("");
  console.log(reversed);
  return x === +reversed;
};

const result = isPalindrome(141);
console.log("result >>>>>>", result);
