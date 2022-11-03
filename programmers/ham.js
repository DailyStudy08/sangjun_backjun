function solution(ingredient) {
    var answer = 0;
    const stack = [];
    for (let i = 0; i < ingredient.length; i++) {
        stack.push(ingredient[i])
        if (stack.length >= 4) {
            if (stack[stack.length-1] == 1 && stack[stack.length-2] == 3 && stack[stack.length-3] == 2 && stack[stack.length-4] == 1) {
                stack.splice(-4, 4)
                answer += 1
            }
        }
    }
    return answer;
}

let ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
console.log(solution(ingredient))
console.log(ingredient)