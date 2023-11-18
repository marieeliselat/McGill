Comp 370 - Homework 2 
Task 2

#Download MariaDB database 
sudo apt install mariadb-server

#make sure MariaDB database is installed properly by running it's security script and creating a pw so that you can log into it 
sudo mysql_secure_installation

#Make it so MariaDB allows external connections by updating the bind-address to equal 0.0.0.0 so that any IP address can access
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf

#restart MariaDB
sudo systemctl restart mariadb

#log into the MariaDB database
sudo mysql -u root -p

#create Database called comp370_test
CREATE DATABASE comp370_test;

#add new user"comp370" with permission to access the database with the password "$ungl@ss3s"
CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';

#Update Security Group Rules to allow port 6002 traffic through
	#Add Inbound rule in the Security Group of the EC2 instance (Type: Custom TCP, 	
	Protocol: TCP, Port Range: 6002, Source: 0.0.0.0/0