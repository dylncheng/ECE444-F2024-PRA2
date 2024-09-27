flasky:
	docker run -d -p 5000:5000 flask-sample

stop:
	docker stop $(docker ps -q)