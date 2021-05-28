## To run locally: 
1. cd app/
2. remove 'from app' part on line 1 of 'from app import gcs, schemas' so its just 'import gcs, schemas'
3. point service-account location on line 46 a local service account json file  eg. service_account = '../service-account'
4. uvicorn main:app --reload

## To deploy to Cloud Run

1. Undo the changes in part 2 and 3 of To run locally
2. make sure you're in the root dir
3. run sh deploy.sh

## To deploy changes to api config on an exisiting API Gateway:

1. gcloud beta api-gateway api-configs create 'CONFIG_NAME'   --api=api-gateway --openapi-spec=openapi2-spec.yaml   --project=halcyonsw --backend-auth-service-account=api-config@halcyonsw.iam.gserviceaccount.com

2. gcloud beta api-gateway gateways update halcyon-api-gateway  --api=api-gateway --api-config='CONFIG_NAME'  --location=us-central1 --project=halcyonsw