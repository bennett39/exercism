export const at = (hour, minute) => {
  const time = rollover(handleFalsy(hour), handleFalsy(minute));
  hour = time.hour;
  minute = time.minute;

  function handleFalsy(digit) { 
    return (digit) ? digit : 0 
  }

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

  return prependZero(hour) + ':' + prependZero(minute);
}


