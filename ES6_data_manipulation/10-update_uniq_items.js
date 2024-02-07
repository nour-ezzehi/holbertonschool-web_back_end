export default function updateUniqueItems(groceries) {
  if (groceries instanceof Map) {
    for (const [key, value] of groceries.entries()) {
      if (value === 1) {
        groceries.set(key, 100);
      }
    }
  } else {
    throw new Error('Cannot process');
  }
  return groceries;
}
