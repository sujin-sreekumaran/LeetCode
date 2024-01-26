/**
 * Checks the validity of brackets in a given string.
 *
 * @param {string} s - The string to check.
 * @return {boolean} The result of the bracket check.
 */
var checkBrackets = function (s) {
  let result = true;

  let Brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  for (let i = 0; i < s.length; i++) {
    if ((Brackets[s[i]] || s[i]) === undefined) {
      result = false;
      break;
    }

    if (Brackets[s[i]] !== s[i + 1] && i % 2 === 0) {
      console.log(i);
      result = false;
      break;
    }
  }

  console.log("Result >>>", result);

  return result;
};

const value = "(";

checkBrackets(value);
