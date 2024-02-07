export default function hasValuesfromArray(set, arr) {
  for (const item of arr) {
    if (!set.has(item)) {
      return false;
    }
  }
  return true;
}
