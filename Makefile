# ==============================================================================
# Define dependencies
# ==============================================================================
AGENTS_APP       := fastagents
BASE_IMAGE_NAME := insidious000
VERSION         := 0.1.0 # Look up pyproject.toml for version; this is just for Docker

# ==============================================================================
# General Commands
# ==============================================================================

init:
	poetry new $(AGENTS_APP)

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
