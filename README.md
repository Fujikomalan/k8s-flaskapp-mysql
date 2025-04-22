``` sh

$ docker run --name mysql_container \
  -d \
  -e MYSQL_ROOT_PASSWORD=mysqlroot123 \
  -p 3306:3306 \
  mysql:latest

$ docker container exec -it mysql_container bash


bash-5.1# mysql -u root -pmysqlroot123

create database college;

use college;

CREATE TABLE students(id int(5),name varchar(255), age int(3),email varchar(255));

INSERT INTO students (id, name,age,email) VALUES(101,"alex",30,"alex@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(102,"don",20,"don@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(103”,"kevin",25,"kevin@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(103,"devon",35,"devon@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(104,"john",42,"john@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(105,"ron",38,"ron@gmail.com");
INSERT INTO students (id, name,age,email) VALUES(106,"thomas",19,"thomas@gmail.com");

create user "appadmin"@"%" identified by "appadmin";
grant all privileges on college.* to "appadmin"@"%";
flush privileges;
```



``` sh
[ec2-user@ip-172-31-0-32 ~]$ docker container run \
  -d \
  --name flask_container \
  -e DATABASE_HOST="3.7.254.73" \
  -e DATABASE_PORT="3306" \
  -e DATABASE_USER="appadmin" \
  -e DATABASE_PASSWORD="appadmin" \
  -e DATABASE_NAME="college" \
  -e DATABASE_TABLE="students" \
  -e FLASK_PORT="8080" \
  -p 8080:8080 \
fujikomalan/k8s-mysql-flaskapp:v1
```
