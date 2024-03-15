SHELL := /bin/bash
.PHONY: help

PROJECT_ID=le-wagon-411314
REGION=us-east1

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	
reinstall_package: ## Reinstall the package
	@pip uninstall -y musicbrain || :
	@pip install -e .

run_backend: ## Run the API
	uvicorn musicbrain.api.fast:app --reload --port 8080

run_frontend: ## Run the API
	streamlit run ./musicbrain-front/userinterface.py

docker_build:
	docker build -f ./musicbrain/Dockerfile . -t musicbrain

docker_build_prod:
	docker build -f ./musicbrain/Dockerfile -t ${REGION}-docker.pkg.dev/${PROJECT_ID}/musicbrain:prod .

docker_push_prod:
	docker push ${REGION}-docker.pkg.dev/${PROJECT_ID}/musicbrain/musicbrain:prod

cloud_run_deploy_prod:
	gcloud run deploy --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/musicbrain/musicbrain:prod --memory 2Gi --region ${REGION} --env-vars-file .env-prod.yaml --port 8080

docker_run:
	docker run --env-file="./.env" -p 8080:8080 musicbrain
