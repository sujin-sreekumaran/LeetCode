var generateParenthesis = async function (n) {
  const result = [];
  await generateParentheses(result, "", 0, 0, n);
  console.log("====================================");
  console.log(result);
  console.log("====================================");
  return result;
};

const generateParentheses = async (result, current, open, close, n) => {
  if (current?.length === 2 * n) {
    result.push(current);
    return;
  }
  if (open < n) {
    await generateParentheses(result, current + "(", open + 1, close, n);
  }
  if (close < open) {
    await generateParentheses(result, current + ")", open, close + 1, n);
  }
};

generateParenthesis(3);
