function rollover(hour, minute) { 
  hour = (hour + Math.floor(minute/60)) % 24;
  minute %= 60;
  if (minute < 0) minute += 60;
  if (hour < 0) hour += 24;
  return {hour: hour, minute: minute}
}

function prependZero(digit) {
  return (digit < 10) ? '0' + String(digit) :  String(digit);
}  

class Clock {
  constructor (hour, minute) {
    const time = rollover(hour, minute);
    this.hour = time.hour;
    this.minute = time.minute;
  }

  toString() {
    return prependZero(this.hour) + ':' + prependZero(this.minute);
  }
}

export const at = (hour, minute = 0) => new Clock(hour, minute);
