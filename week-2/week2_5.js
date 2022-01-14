function maxZeros(nums){
    let zero_cnt=0;
    let max_cnt=0;
    for(let i=0; i<nums.length;i++){
        if(nums[i]==0){
            zero_cnt+=1;
        }
        if(zero_cnt>max_cnt){
            max_cnt=zero_cnt;
        }
        if(nums[i]==1){
            zero_cnt=0;
        }
    }
    console.log(max_cnt)
}

maxZeros([0, 1, 0, 0]); //2
maxZeros([1, 0, 0, 0 ,0 ,1, 0, 1, 0, 0]); //4
maxZeros([1, 1, 1, 1, 1]); //0
maxZeros([0, 0, 0, 1, 1]) //3