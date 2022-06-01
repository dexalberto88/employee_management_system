# Employee Management System - Django

## Overview
Employee management system application using Django.
- Functionalities
	 - Employee login, logout 
	 - Time logs
	 	 - Record time in, time out
		 - Delete time logs
		 - View total time logs per day
	- Managements
		- Staff user can view, add, update, delete:
			- Employees
			- Departments
			- Job Role
	 - Profile
		 - User can view and update profile
- Responsive web design

## Prerequisites
 - Linux OS (mint, ubuntu)
 - Django
 - Python3
 - Docker

## Development
1. Install [docker](https://docs.docker.com/engine/install/ubuntu/)
```bash
sudo apt update
sudo apt install -y docker.io
sudo groupadd docker
sudo usermod -aG docker $USER
# Close terminal and open new one
docker run hello-world # to check
```
2. Create docker container
```bash
docker pull ubuntu:20.04
docker run -v ~/shared_folder:/root/shared_folder \
--cap-add=NET_ADMIN --name "my-ubuntu" -w "/root" -it "ubuntu:20.04"
```
3. Install [python3](https://www.python.org/downloads/) and pip
```bash
cd ~
apt update
# Install python3 option #1 by apt
apt install -y python3
# Install python3 option #2 by source
apt install -y wget
wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tar.xz
apt install -y xz-utils gcc g++ make
tar -xf Python-3.10.4.tar.xz
cd Python-3.10.4/
./configure
make
make test
make install
# Check python version
python3 --version
# Install pip
apt install -y python3-pip
pip --version
```
4. Install python [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
```bash
# pip install virtualenv
apt install python3-venv
pip list
```
5. Create python virtual environment
```bash
cd ~/shared_folder/
python3 -m venv env
source env/bin/activate
# To deactivate run: deactivate
```
6. Install [Django](https://www.djangoproject.com/download/)
```bash
pip install Django==4.0.4
python -m django --version
```
7. Create Django [project](https://www.djangoproject.com/start/)
```bash
django-admin startproject mysite
cd mysite/
```
8. Test run
```bash
python manage.py runserver # on host machine
# or
python manage.py runserver 0.0.0.0:8000 # on docker container
# For error 'No time zone found with key UTC' run: pip install tzdata
# For error Invalid HTTP_HOST header: '172.17.0.2:8000'. You may need to add '172.17.0.2' to ALLOWED_HOSTS. add: ALLOWED_HOSTS = ['*'] in mysite/settings.py
```

## Build and Run
```bash
cd ~
git clone https://github.com/dexalberto88/employee-management-system.git
python3 -m venv env
source env/bin/activate
cd employee-management-system/
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver 0:8000
# Open http://<ip>:8000 in web browser
# Ex. http://172.17.0.2:8000
```

## Usage
1. Open http://172.17.0.x:8000/admin/
2. Login using superuser account
3. Create at least 1 staff user
4. Logout in admin
5. Go to http://172.17.0.x:8000/
6. Login using staff user and add new Employees
7. Staff and Employees can now use the system
8. That's it! cheers!

## Screenshots
![Login](https://lh3.googleusercontent.com/pw/AM-JKLXFzBiOITrx9qu-FGePH3f-LKFE4rTy68j_aUwSIl4_MP-yKCOLkrWAlnyiYZjsw29GtOhbZswm11N_309vn4K-Bf6lc-1uL4itXYALJGEYYrHQzGxg-rELdcqL10usGo8px2wdNhr7lVWpScrrYP6g=w1221-h865-no?authuser=0)

![enter image description here](https://lh3.googleusercontent.com/pw/AM-JKLUXnwLWp1soZ-woBy7xS_A-FEIXte0IUSVaLUyGA7avLsUwFYqWSls_ZsoF4Qz_zuU5QAx3GvXXwY2IXmyMNZuEcYKIl2ZTUDQP2D212j28iPoN5rB7cvH79jAd7l4yX0h_9KbEc4zVaPKDFsaCJZYd=w1221-h865-no?authuser=0)

![enter image description here](https://lh3.googleusercontent.com/pw/AM-JKLX4OrlaHJNq-xJia0dVKWlZL7wVcWlFadyMBY3bQIiw30XUK7koVU0j73S3zHqR4JbpFwyb5OIKwMxLJttrxJiU4p1bH0yiDY9NEmJ5VBF0ef949G82JZh2UMpG5McKXARCGQcDNFmZvKofIU2qb6PZ=w1221-h865-no?authuser=0)

![enter image description here](https://lh3.googleusercontent.com/pw/AM-JKLW8Wl7aiZJ7kJagFyCLKrt_AYIkqd-ePf8UONmRILkrhToVSGXzBQygeVEF3X9Sj1FrYRmxLOy20_hrmLYpJOKSpP_OIgHpjKyrB2u0rSVdzWpiphjbE1lpm-yocPcJtGSs5a8x2KdiUoQeOBKjf7Dr=w1221-h865-no?authuser=0)

![enter image description here](https://lh3.googleusercontent.com/pw/AM-JKLXWM8sct4-FVSTq-souvrgYmkQWFMR9rv3AKzA8SBx_ArZs4zodLXQFGy6e0cPVps4rC6C6SbZ-wsQlxH1oRbiLPey_vsLQL_xXAZwFItkLqxzXsV7U0BPH0p6rEu5dwwZguIwZMijHvOpWt0r2-UZP=w1221-h865-no?authuser=0)

### Errors and fixes
 - Time zone error in docker
	 - pip install tzdata

### Disclaimers
 - Ongoing updates and improvements