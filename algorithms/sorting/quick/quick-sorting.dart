void main() {
  List<int> array = [
    70,
    93,
    66,
    9,
    48,
    77,
    55,
    56,
    74,
    56,
    31,
    84,
    84,
    17,
    22,
    16,
    69,
    45,
    90,
    96,
    56,
    50,
    40,
    19,
    35,
    11,
    73,
    73,
    89,
    16,
    63,
    59,
    9,
    29,
    67,
    56,
    6,
    21,
    11,
    79,
    76,
    42,
    62,
    60,
    59,
    84,
    76,
    27,
    29,
    65
  ];
  print(quick(array, 0, array.length - 1));
}

List<int> quick(List<int> array, int left, int right) {
  var index;

  if (array.length > 1) {
    index = partition(array, left, right);

    if (left < index - 1) {
      quick(array, left, index - 1);
    }
    if (index < right) {
      quick(array, index, right);
    }
  }

  return array;
}

int partition(List<int> array, int left, int right) {
  var pivot = array[((right + left) / 2).floor()];

  var i = left;
  var j = right;

  while (i <= j) {
    while (array[i] < pivot) {
      i++;
    }
    while (array[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(array, i, j);
      i++;
      j--;
    }
  }

  return i;
}

void swap(List<int> array, int index1, int index2) {
  var tmp = array[index1];
  array[index1] = array[index2];
  array[index2] = tmp;
}
