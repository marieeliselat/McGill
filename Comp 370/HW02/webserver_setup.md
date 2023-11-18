Comp 370 - Homework 2 
Task 1
#Install apache
sudo apt install apache2

#Allow incoming HTTP traffic on port 8008
sudo ufw allow 8008/tcp

#Add Listen directive by opening the apache ports.conf file and adding at the end "Listen 8008" and "DocumentRoot /www" (to let the apache web server serve files located in the '/var/www/html' directory of my server)
sudo vim /etc/apache2/ports.conf

#Modify Virtual host to let it listen on port 8008 by changing "<VirtualHost *:80>" to "VirtualHost *:8008>"
sudo vim /etc/apache2/sites-available/000-default.conf

#Restart Apache to make sure all the changes have been applied 
sudo systemctl restart apache2

#create comp370_hw2.txt
echo "I will get a good grade in COMP 370 :-)" | sudo tee /www/comp370_hw2.txt

#Update Security Group Rules to allow port 8008 traffic through
	#Add Inbound rule in the Security Group of the EC2 instance (Type: Custom TCP, 	
	Protocol: TCP, Port Range: 8008, Source: 0.0.0.0/0

#test to at http://X.Y.Z.W:8008/comp370_hw2.txt
#For me it was http://18.191.49.83:8008/comp370_hw2.txt


