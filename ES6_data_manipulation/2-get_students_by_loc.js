export default function getStudentsByLocation(arr, city) {
  const newArr = arr.filter((obj) => obj.location === city);
  return newArr;
}
