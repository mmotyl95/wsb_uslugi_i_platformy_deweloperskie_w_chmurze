# WSB Project Cloud App

**README**

Project by Michał Motyl - Simple Flask web app


## Development

1. Logging into Azure 
``` az login```
2. Creating resource
```az group create -n project_wsb -l westeurope```
3. Creating virtual machine
```az vm create --resource-group project_wsb --name simple_app --size "Standard_B1ls" --image "Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest" --public-ip-sku Standard --admin-username ubuntu```
4. Connecting to the virtual machine with ssh (it can be found in field "publicIpAddress")
```ssh ubuntu@<**your_ip_address**>```
	
6. Install docker and git 

```sudo apt-get install docker.io``` 

```sudo apt-get install git```

1. Clone repository 
```git clone git@github.com:mmotyl95/wsb_uslugi_i_platformy_deweloperskie_w_chmurze.git```

8. Go to app directory
   `cd wsb_uslugi_i_platformy_deweloperskie_w_chmurze/projekt/app/`


## Preparing and running dockerized app

1. Build docker image from Dockerfile
```docker run -t docker-python .```
2. Run our project
```docker container run -p 5000:5000 docker-python ```
3. Check if the project is avaliable on localhost

```curl localhost:5000```

```curl localhost/hello:5000```

```curl localhost/hello/you_name:5000```

An output should be like:
```
$ curl localhost:5000
Witam na stronie projektu
```