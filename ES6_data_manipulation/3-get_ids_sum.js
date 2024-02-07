export default function getStudentIdsSum(arr) {
  return arr.reduce((total, obj) => total + obj.id, 0);
}
