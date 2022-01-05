def avg(data):
    num = data.get("count")
    sum = 0
    for i in range(num):
        sum += data.get("employees")[i].get("salary")
        mean = sum / num
    print(mean)

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