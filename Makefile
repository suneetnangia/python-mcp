# Makefile for Python MCP Server

.PHONY: help install run test format lint clean

help:
	@echo "Available commands:"
	@echo "  install    Install dependencies"
	@echo "  run        Run the MCP server"
	@echo "  test       Run tests"
	@echo "  format     Format code with black"
	@echo "  lint       Lint code with flake8"
	@echo "  clean      Clean up temporary files"

install:
	pip install -r requirements.txt

run:
	python server.py

test:
	python -m pytest -v

format:
	black *.py --line-length=88

lint:
	flake8 *.py --max-line-length=88

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
