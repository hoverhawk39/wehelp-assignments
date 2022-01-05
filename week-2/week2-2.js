function avg(data){
    let num=data.count
    let sum=0
    for(let i=0; i<num; i++){
        sum += data.employees[i].salary
    }
    let avg=sum/num
    console.log(avg)
}
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})