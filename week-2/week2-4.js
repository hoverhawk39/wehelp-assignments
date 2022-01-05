function twoSum(nums, target){
    let num=nums.length
    for(let i=0; i<num; i++){
        let a1=target-nums[i]
        if(a1>0){
            for(let j=i+1; j<num; j++){
                if(nums[j]==a1){
                    let ans=[]
                    ans.push(i,j)
                    return ans
                }
            }
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result);