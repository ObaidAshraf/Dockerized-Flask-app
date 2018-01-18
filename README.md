## Dockerized-Flask-app
### Platform:
* Windows 10 Home (64-bit)
* Docker toolbox

### Steps:
* Create a Flask application with requirements.txt and Dockerfile.
* Build docker image to verify if the image is working correctly or not. 
* Following are the commands I used to build and test the image. 
* Make sure that you are in the same directory where your project files (python source files, requriements.txt and Dockerfile) are placed. Following are the commands:
```
docker pull python
```
```
docker image built -t weather_app . 
```
```
docker container run -d -p 3000:5000 --name weaAppweather_app
```
From the above command, your newly built image will be run as “daemon” and you can check on your localhost:3000. But, in case of Docker Toolbox, you can’t check on localhost:3000. It is because Docker toolbox uses VM and everything is to be accessed via this VM’s IP.
You can get Docker VM’s IP using:
```
Docker-machine ip
```
Now, if above command returns IP as “192.168.99.100” then, you can use below address to access your Flask app. http://192.168.99.100:3000/

* Uploading on docker hub is quite easy and it requires some basic steps as follows:
```
docker  login (Login to your docker hub account)
```
```
docker tag weather_app<username>/<image_name>:<tag>
(With the above command, you can tag your pre-built image, in our case the image we just built. Tagging convention is according to docker hub which is mentioned in their Wiki)
```
```
docker push <username>/<image_name>
```
