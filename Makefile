# ==============================================================================
# Define dependencies
# ==============================================================================
MEETX_APP       := fastagents
BASE_IMAGE_NAME := insidious000
VERSION         := 0.1.0 # Look up pyproject.toml for version; this is just for Docker
API_IMAGE       := $(BASE_IMAGE_NAME)/$(MEETX_APP):$(VERSION)

# ==============================================================================
# General Commands
# ==============================================================================

init:
	poetry new $(MEETX_APP)

track-tree:
	poetry show --tree

track-latest:
	poetry show --latest

install:
	poetry add $(cat requirements.txt)

update:
	poetry update package

dev-install:
	poetry add --dev ruff

reqs:
		pip3 install -r requirements.txt --index-url https://pypi.doubanio.com/simple/pip3 install -r requirements.txt

run:
	# Stop any process using port 9000
	lsof -i :9000 | awk 'NR!=1 {print $$2}' | xargs -r kill -9
	# Run the FastAPI app
	python3 run.py

build:
	poetry build

# Use this when package is removed
lock:
	poetry lock

ruff:
	ruff check

# ==============================================================================
# Versioning
# ==============================================================================

version:
	@if [ -z "$(SEMVER)" ]; then \
		poetry version; \
	else \
		poetry version $(SEMVER); \
	fi

version-help:
	@echo "Usage: make version SEMVER=<bump_type>"
	@echo ""
	@echo "Available bump types:"
	@echo "  show         Show current version"
	@echo "  patch        Bump patch version (0.0.X)"
	@echo "  minor        Bump minor version (0.X.0)"
	@echo "  major        Bump major version (X.0.0)"
	@echo "  preminor     Bump preminor version (0.X.0a0)"
	@echo "  premajor     Bump premajor version (X.0.0a0)"
	@echo "  prerelease   Bump prerelease version (0.0.0aX)"

# ==============================================================================
# Docker
# ==============================================================================

docker-build: meetx

meetx:
	docker build \
		-f zarf/docker/dockerfile.meetx \
		-t $(API_IMAGE) \
		--build-arg BUILD_REF=$(VERSION) \
		--build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
		.

docker-run:
	docker run -d \
		--name meetx-api \
		-p 8080:8080 \
		$(API_IMAGE)

docker-push:
	# Log in to Docker
	docker login

	# Build and push the Docker image
	docker build \
		--platform=linux/amd64 \
		-f zarf/docker/dockerfile.genai \
		-t $(API_IMAGE) \
		--build-arg BUILD_REF=$(VERSION) \
		--build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
		.
	docker push insidious000/meetx-genai-service:$(VERSION)
	
	# Build and push the latest image as well
	docker build \
		--platform=linux/amd64 \
		-f zarf/docker/dockerfile.genai \
		-t $(API_IMAGE) \
		-t $(BASE_IMAGE_NAME)/$(MEETX_APP):latest \
		--build-arg BUILD_REF=$(VERSION) \
		--build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
		.
	docker push insidious000/meetx-genai-service:latest

# UVICORN command (commented out)
# uvicorn main:app --reload
