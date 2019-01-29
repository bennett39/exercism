export class Triangle {
  constructor(a, b, c) { this.a = a; this.b = b; this.c = c; }
  kind() {
    const [a, b, c] = [this.a, this.b, this.c];
    if (a + b > c && a + c > b && b + c > a) {
      if (a === b && b === c) return 'equilateral';
      else if (a === b || a === c || b === c) return 'isosceles';
      return 'scalene';
    }
    throw 'Not a triangle';
  }
}

