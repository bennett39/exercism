function prependZero(digit) {
  return (digit < 10) ? '0' + String(digit) :  String(digit);
}  

class Clock {
  constructor (hour, minute) {
    let time = hour * 60 + minute;
    const day = 24 * 60;

    while (time < 0) time += day;

    this.hour = Math.floor((time % day) / 60);
    this.minute = time % 60;

    this.toString = () => {
      return [this.hour, this.minute].map(prependZero).join(':');
    }

    this.plus = (minutes) => {
      return new this.constructor(this.hour, this.minute + minutes);
    }

    this.minus = (minutes) => {
      return new this.constructor(this.hour, this.minute - minutes);
    }

    this.equals = (other) => this.toString() === other.toString()
  }
}

export const at = (hour, minute = 0) => new Clock(hour, minute);
