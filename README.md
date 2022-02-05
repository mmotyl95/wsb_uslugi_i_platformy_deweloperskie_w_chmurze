# .WSB Project Cloud App

**README TESTOWY, ZOSTANIE UZUPEŁNONY O RZECZYWISTY PROJEKT**

This is my project for Usługi i platformy deweloperskie dla aplikacji w Chmurze


## Development

1. Logging into Azure 
<code> az login</code>
2. Creating resource
<code>az group create -n project_wsb -l westeurope</code>
3. Creating virtual machine
<code>az vm create --resource-group project_wsb --name simple_app --size "Standard_B1ls" --image "Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest" --public-ip-sku Standard --admin-username ubuntu</code>
4. Connecting to the virtual machine with ssh (it can be found in field "publicIpAddress")
<code>ssh ubuntu@<**your_ip_address**></code>
	
6. Install docker and git 
<code>sudo apt-get install docker.io</code><code>sudo apt-get install git</code>
7. Clone repository 
<code>git clone git@github.com:mmotyl95/wsb_uslugi_i_platformy_deweloperskie_w_chmurze.git</code>

## Preparing and running dockerized app
1. Build docker image from Dockerfile
<code>docker run -t docker-python<code>
2. Run our project
<code>docker container run -p 5000:5000 docker-python .</code>
3. Check if the project is avaliable on localhost
<code>curl localhost:5000</code>
<code>curl localhost/hello:5000</code>
<code>curl localhost/hello/you_name:5000</code>

