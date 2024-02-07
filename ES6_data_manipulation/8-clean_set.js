export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const sets = [];
  set.forEach((item) => {
    if (item.startsWith(startString)) {
      sets.push(item.slice(startString.length));
    }
  });
  return sets.join('-');
}
