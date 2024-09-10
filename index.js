const linearSearch = (arr, target) => {
  const index = arr.indexOf(target);
  return index !== -1 ? index : null;
};

const binarySearch = (arr, target) => {
  let [first, last] = [0, arr.length - 1];

  //if (arr[last] == target) return last;
  while (first <= last) {
    const midpoint = Math.floor((first + last) / 2);
    console.log(midpoint, first);
    if (arr[midpoint] === target) return midpoint;
    else if (arr[midpoint] < target) {
      first = midpoint;
    } else if (arr[midpoint] > target) {
      last = midpoint;
    } else return `${target} not in ${arr}`;
  }
};
const ans = binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 8);
console.log(ans);
