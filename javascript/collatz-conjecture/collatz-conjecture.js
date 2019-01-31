export const steps = n => {
  if (n < 1) throw new Error('Only positive numbers are allowed');
  return collatz(n);
}

function collatz(n, steps = 0){
  if (n === 1) return steps; 
  (n % 2 === 0) ? n /= 2 : n = 3 * n + 1;
  steps++;
  return collatz(n, steps);
}
