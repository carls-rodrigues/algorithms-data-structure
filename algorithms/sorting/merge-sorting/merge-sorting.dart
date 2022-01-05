const array = [
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
void main(List<String> args) {
  print(mergeSort(array));
}

List<int> mergeSort(List<int> array) {
  int length = array.length;
  if (length == 1) {
    return array;
  }

  int mid = (length / 2).floor();

  List<int> left = array.sublist(0, mid);
  List<int> right = array.sublist(mid, length);

  return merge(mergeSort(left), mergeSort(right));
}

List<int> merge(List<int> left, List<int> right) {
  List<int> result = [];
  int il = 0;
  int ir = 0;

  while (il < left.length && ir < right.length) {
    if (left[il] < right[ir]) {
      result.add(left[il++]);
    } else {
      result.add(right[ir++]);
    }
  }

  while (il < left.length) {
    result.add(left[il++]);
  }
  while (ir < right.length) {
    result.add(right[ir++]);
  }
  return result;
}
