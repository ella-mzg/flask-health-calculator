APP_NAME = health-calculator
IMAGE_NAME = $(APP_NAME)
PORT = 5000

.PHONY: init run test build clean

# Initialize the environment
init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run the application
run:
	@echo "Running Flask application..."
	python app.py

# Test the application
test:
	@echo "Running tests..."
	python -m unittest discover

# Build the Docker image
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
docker-run:
	@echo "Running Docker container..."
	docker run -p $(PORT):5000 $(IMAGE_NAME)

# Clean up Docker images
clean:
	@echo "Cleaning up Docker images..."
	docker rmi $(IMAGE_NAME)
