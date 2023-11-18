Comp 370 - Homework 2 
Task 2

__#Download MariaDB database__  
sudo apt install mariadb-server

__#Make sure MariaDB database is installed properly by running it's security script and creating a pw so that you can log into it__   
sudo mysql_secure_installation

__#Make it so MariaDB allows external connections by updating the bind-address to equal 0.0.0.0 so that any IP address can access__  
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf

__#Restart MariaDB__  
sudo systemctl restart mariadb

__#Log into the MariaDB database__  
sudo mysql -u root -p

__#Create Database called comp370_test__  
CREATE DATABASE comp370_test;

__#Add new user"comp370" with permission to access the database with the password "$ungl@ss3s"__  
CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';

__#Update Security Group Rules to allow port 6002 traffic through__  
__#Add Inbound rule in the Security Group of the EC2 instance (Type: Custom TCP,Protocol: TCP, Port Range: 6002, Source: 0.0.0.0/0)__
