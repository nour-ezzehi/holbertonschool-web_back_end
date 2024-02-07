export default function updateStudentGradeByCity(arr, city, newGrades) {
  const newArr = arr.filter((obj) => obj.location === city).map((obj) => {
    const [grade] = newGrades.filter((gradeObj) => gradeObj.studentId === obj.id);
    if (grade) {
      return { ...obj, grade: grade.grade };
    }
    return { ...obj, grade: 'N/A' };
  });
  return newArr;
}
