# dataeng-project




# GCP-Secrets
- Once you have the service account file downloaded, you can rename it to service-account.json. Then we'll encode the service account JSON and store it inside of a file named .env_encoded which will hold all of our encoded secrets:
- -w 0 is unnecessary on mac as base64 on mac handles line wrapping 
```
echo SECRET_GCP_SERVICE_ACCOUNT=$(cat service-account.json | base64 -w 0) >> .env_encoded
```