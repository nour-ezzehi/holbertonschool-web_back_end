export default function getListStudentsIds(arr) {
  if (Array.isArray(arr)) {
    const newArr = arr.map((obj) => obj.id);
    return newArr;
  }
  return [];
}
