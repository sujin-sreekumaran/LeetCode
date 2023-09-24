/**
 * Converts a Roman numeral string to an integer.
 *
 * @param {string} s - The Roman numeral string to convert.
 * @return {number} The integer value of the Roman numeral string.
 */
var romanToInt = function (s) {
  const sym = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let result = 0;

  for (let i = 0; i < s.length; i++) {
    const cur = sym[s[i]];
    const next = sym[s[i + 1]];

    if (cur < next) {
      result += next - cur;
      i++;
    } else {
      result += cur;
    }
  }

  console.log("Result >>>", result);

  return result;
};

const value = "XML";

romanToInt(value);
