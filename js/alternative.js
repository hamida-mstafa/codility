function solution(A) {
    const input = String(A);
    const length = input.length;
    const shuffled = [];
    let front = 0, back = length - 1;
    while (front <= back) {
      shuffled.push(input.charAt(front++));
      if (front <= back) {
        shuffled.push(input.charAt(back--));
      }
    }
    return Number(shuffled.join(''));}