function calcDistCenter(x, y) {
  return Math.sqrt((x * x) + (y * y));
}

function givePointsByDist(distance) {
  if (distance <= 1) { return 10; }
  else if (1 < distance && distance <= 5) { return 5; }
  else if (5 < distance && distance <= 10) { return 1; }
  else if (distance > 10) { return 0; }
  return null;
}

export const solve = (x, y) => {
  const distance = calcDistCenter(x, y);
  return givePointsByDist(distance);
}
