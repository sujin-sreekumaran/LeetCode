const roman = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const value = "MCMXCIV";

/**
 * Converts a Roman numeral string to an integer value.
 *
 * @param {string} value - The Roman numeral string to be converted.
 * @return {number} - The integer value equivalent of the Roman numeral string.
 */
const romanToInt = (value) => {
  let s = value.split("");

  for (let i = 0; i < s.length; i++) {
    s[i] = roman[s[i]];
    if (s[i] != roman.I) {
      
    }
  }
  const result = s.reduce((a, b) => a + b);

  console.log("====================================");
  console.log(result);
  console.log("====================================");

  return result;
};

romanToInt(value);
