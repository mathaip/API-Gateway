gcloud builds submit --tag gcr.io/halcyonsw/api-gateway

gcloud run deploy api-gateway --image gcr.io/halcyonsw/api-gateway --set-env-vars Service_Account=service-account.json --region us-central1 --platform managed