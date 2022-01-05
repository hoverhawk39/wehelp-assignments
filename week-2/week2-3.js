function maxProduct(nums){
    let num = nums.length
    let r1=[]
    for(let i=0; i<num; i++){
        for(let j=0; j<num; j++){
            if(i!==j){
                let mul=nums[i]*nums[j]
                r1.push(mul)
            }
        }
    }
    // console.log(r1)
    let ans=Math.max(...r1)
    console.log(ans)
}
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])