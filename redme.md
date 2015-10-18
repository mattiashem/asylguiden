How to setup on a new server


Ubuntu on AWS

open
vi /etc/apt/sources.list.d/docker.list

add correct
# Ubuntu Precise
deb https://apt.dockerproject.org/repo ubuntu-precise main
# Ubuntu Trusty
deb https://apt.dockerproject.org/repo ubuntu-trusty main
# Ubuntu Vivid
deb https://apt.dockerproject.org/repo ubuntu-vivid main
# Ubuntu Wily
deb https://apt.dockerproject.org/repo ubuntu-wily main


install key
apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D


install docker
apt-get install docker-engine

fix user
sudo usermod -aG docker ubuntu

Docker compose
curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose



Now you can run docker compos and use the plattform