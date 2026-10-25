.DEFAULT_GOAL := help

.PHONY: help lint format typecheck security complexity check install

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-20s %s\n", $$1, $$2}'

install: ## Install project and development dependencies
	poetry install

lint: ## Run Ruff linter
	poetry run ruff check src tests

format: ## Run Ruff Formatter
	poetry run ruff format src tests

typecheck: ## Run mypy
	poetry run mypy src

test: ## Run tests
	poetry run pytest

complexity: ## Run cyclomatic complexity check
	poetry run radon cc src -s -a

security: ## Run security check
	poetry run bandit -r src -ll

check: lint format typecheck test complexity security
