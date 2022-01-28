### 作業三
【1】
>insert into member(name,username,password,follower_count) values("Sam","test","test",100); <br/>
>insert into member(name,username,password,follower_count) values("Jay","test2","test2",200); <br/>
>insert into member(name,username,password,follower_count) values("Mark","test3","test3",300); <br/>
>insert into member(name,username,password,follower_count) values("Winnie","test4","test4",400); <br/>
>insert into member(name,username,password,follower_count) values("Peter","test5","test5",500); <br/>
>insert into member(name,username,password,follower_count) values("Vanson","test6","test6",600);

![](https://i.imgur.com/Rn7P7oY.png)


【2】

>SELECT * from member;

![](https://i.imgur.com/cQeGiYm.png)


【3】
>SELECT *
>FROM member
>ORDER BY time DESC;

![](https://i.imgur.com/r05mXZJ.png)


【4】
>SELECT *
>FROM member
>ORDER BY time DESC
>LIMIT 1,3;

![](https://i.imgur.com/zJQrYFf.png)


【5】
>SELECT *
>FROM member
>WHERE username="test";

![](https://i.imgur.com/O5EUhtw.png)


【6】
>SELECT *
>FROM member
>WHERE username="test" and password="test";

![](https://i.imgur.com/OibkmHz.png)


【7】
>UPDATE member
>SET name = "test2"
>WHERE username = "test";

![](https://i.imgur.com/o7VNVoy.png)


### 作業四
【1】
>SELECT COUNT(*) AS total_data
>FROM member;

![](https://i.imgur.com/ox53X5a.png)


【2】
>SELECT SUM(follower_count) AS sum_of_follower
>FROM member;

![](https://i.imgur.com/r4n5Zp3.png)


【3】
>SELECT AVG(follower_count) AS avg_of_follower
>FROM member;

![](https://i.imgur.com/ATzYhpw.png)


### 作業五
>USE website;
>CREATE TABLE message(id BIGINT AUTO_INCREMENT,
>	member_id BIGINT NOT NULL,
>	content VARCHAR(255) NOT NULL,
>    time DATETIME NOT NULL default current_timestamp,
>    PRIMARY KEY (id),
>    FOREIGN KEY (member_id) REFERENCES member(id)
>)ENGINE=InnoDB DEFAULT CHARSET=utf8;

建立完 message 資料表，用 desc 查看表格概況～

![](https://i.imgur.com/Xr5BXHa.png)

隨意新增五筆資料之後～

![](https://i.imgur.com/KQx0PSX.png)


【1】
>SELECT content,name
>FROM website.message mes LEFT JOIN website.member mem
>ON mes.member_id=mem.id;

![](https://i.imgur.com/cnFLBNw.png)


【2】
>SELECT username,content,name
>FROM website.message mes LEFT JOIN website.member mem
>ON mes.member_id=mem.id
>HAVING mem.username="test";

![](https://i.imgur.com/FNOS9o8.png)
