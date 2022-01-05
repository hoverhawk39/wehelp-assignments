function calculate(min, max){
    let ans=0
    for(let i=min; i<=max; i++){
        ans += i
    }
    console.log(ans)
}
calculate(1,3);
calculate(4,8);