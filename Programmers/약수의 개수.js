function findNumber (num){
    let count = 0
    for(let i = 1 ; i <= num ; i++ ){
        if ( num % i === 0){
            count += 1
        }
    }
    return count
}

function solution(left, right) {
    var answer = 0;
    for( let i = left ; i <= right ; i++){
        if(findNumber(i) % 2 === 0 ){
            answer += i
        }else{
            answer -= i
        }
    }
    return answer;
}
