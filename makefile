.PHONY: install run clean

install:
	# Create a virtual environment for InfraVille API
	python3 -m venv ./venv
	# Activate the virtual environment and install dependencies
	./venv/bin/pip install -r ./requirements.txt

run:
	# Activate the virtual environment and run the application
	./venv/bin/python ./src/app.py

lint:
	# Activate the virtual environment and run pylint
	./venv/bin/flake8 ./src/app.py
	
clean:
	# Remove the virtual environment
	rm -rf ./venv
	rm -rf ./__pycache__
	rm -rf ./.pytest_cache
	rm -rf ./tests/__pycache__
	rm -rf ./tests/*.pyc

freeze:
	# Freeze the dependencies
	./venv/bin/pip freeze > requirements.txt

build:
	# Build the docker image
	docker build -t lettergridgen .

docker-run:
	# Run the docker image
	docker run -p 8080:8080 --rm --name lettergridgen-container lettergridgen

docker-tag:
	# Tag the docker image
	docker tag lettergridgen:latest gcr.io/wordrivalry/lettergridgen:latest

docker-push:
	# Push the docker image to Google Cloud Registry
	docker push gcr.io/wordrivalry/lettergridgen:latest

docker-deploy: build docker-tag docker-push
	# Deploy the docker image to Google Cloud Run
	gcloud run deploy lettergridgen --image gcr.io/wordrivalry/lettergridgen:latest --platform managed --allow-unauthenticated
