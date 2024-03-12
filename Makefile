SHELL := /bin/bash
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	
reinstall_package: ## Reinstall the package
	@pip uninstall -y musicbrain || :
	@pip install -e .

run_api: ## Run the API
	uvicorn musicbrain.api.fast:app --reload
