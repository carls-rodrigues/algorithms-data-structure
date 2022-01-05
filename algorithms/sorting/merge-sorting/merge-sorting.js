const array = [70, 93, 66, 9, 48, 77, 55, 56, 74, 56,
  31, 84, 84, 17, 22, 16, 69, 45, 90, 96,
  56, 50, 40, 19, 35, 11, 73, 73, 89, 16,
  63, 59, 9, 29, 67, 56, 6, 21, 11, 79,
  76, 42, 62, 60, 59, 84, 76, 27, 29, 65
];


const mergeSort = (array) => {
  let length = array.length

  if (array.length === 1) return array

  let mid = Math.floor(length / 2)
  let left = array.slice(0, mid)
  let right = array.slice(mid, length)


  return merge(mergeSort(left), mergeSort(right))
}

const merge = (left, right) => {
  let result = []
  let il = 0;
  let ir = 0;

  while (il < left.length && ir < right.length) {
    if (left[il] < right[ir]) {
      result.push(left[il++])
    } else {
      result.push(right[ir++])
    }
  }

  while (il < left.length) {
    result.push(left[il++])
  }
  while (ir < right.length) {
    result.push(right[ir++])
  }

  return result
}

console.log(mergeSort(array))