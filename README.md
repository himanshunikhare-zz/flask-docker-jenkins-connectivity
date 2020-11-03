# flask-docker-jenkins-connectivity

A very simple blog application in flask build over docker to show its connectivity with jenkins

Clone this project using the command:
```
    git clone https://github.com/himanshunikhare/flask-docker-jenkins-connectivity.git
```
# How to run


Build image from **dockerfile**
```
    docker build -t my_docker_flask:latest .
```
Run  docker **image** build using above command
```
    docker run -d -p 5000:5000 my_docker_flask:latest
```
Open your favourite browser and paste the below link:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
# Creating and CI/CD pipeline

- Install and run jenkins in localhost
	- 
	using [this official](https://www.jenkins.io/doc/book/installing/) documentation.

		In my case being an arch user, i followed [this article](https://computingforgeeks.com/how-to-install-and-configure-jenkins-on-arch-linux/) to install and run jenkins

- Expose your localhost using [ngrok](https://ngrok.com/docs)
	- 

	Download [ngrok](https://ngrok.com/) and run:
	
	```
	ngrok http 8090
	```
- Create a github webhook
	- 


# Technology used:

 - Docker
	 - 
	 Docker is an application build and deployment tool. It is based on the idea of that you can package your code with dependencies into a deployable unit called a container.
	 
 - Flask 
	 - 
	 Flask_ is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications
	
	 
 - Jenkins
	 - 
	 Jenkins_ – an open source automation server which enables developers around the world to reliably build, test, and deploy their software.
	 
- Ngrok
	- 
	Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels.
