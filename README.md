# ScalableServices_MovieRatingApp

This is a movie rating application built with python and flask using mysql db. It demonstrates simple microservices using api where data is fetched from the database
or user is allowed to enter the rating for a movie and in addition the user can check few ratings which are rendered in a table format that is read from a csv.

#Below are the steps involved. 

pip install flask
pip install flask
pip install mysql-connector-python

#to run application 
python app.py 

#configure db details in a seperate config file or provide in main file. 

#or create a virtual env and run from there
python -m venv new-env
\new-env\Scripts\Activate.ps1

#Freeze the requirements 
pip freeze > requirements.txt

#create docker file and build and run as below
docker build -t scalable_second .
docker run --name=docconnew123 -d -p 5000:5000 scalable_second 

#verify using below
docker images
docker ps

#deploy application in minikube /kubernetes 
#install minikube and kubectl
minikube start
kubectl create deployment scalaassignew --image=scalable_second/movie-appnew:1.0
kubectl expose deployment scalaassignew --type=NodePort --port=3030
kubectl get service scalaassignew
minikube service scalaassignew --url

