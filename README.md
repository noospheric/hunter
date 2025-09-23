# Outwize Streamlit App

Outwize is a recruiting experience that helps teams discover, vet, and hire specialized AI agents. The Streamlit app highlights the brand, key features, and an embedded Typebot flow that lets visitors start a hiring conversation.

## Live App

Visit the deployed app at https://outwize.streamlit.app/

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Launch the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

## Deploy to Google Cloud Run

1. Build and push the container image with Cloud Build:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/outwize-streamlit
   ```
2. Deploy the service to Cloud Run (replace the project id if needed):
   ```bash
   gcloud run deploy outwize-streamlit \
       --image gcr.io/YOUR_PROJECT_ID/outwize-streamlit \
       --region europe-west1 \
       --platform managed \
       --allow-unauthenticated
   ```
3. Fetch the service URL once deployment finishes:
   ```bash
   gcloud run services describe outwize-streamlit \
       --region europe-west1 \
       --format='value(status.url)'
   ```

Environment configuration (for example API keys) can be sourced from Secret Manager and exposed as environment variables via `--update-secrets`.

## App Highlights

- Custom hero layout and styling that matches the Outwize brand
- Dual call-to-action buttons for hiring and getting hired
- Embedded Typebot conversation that appears after the Hire interaction
- Expandable sections detailing how Outwize works and the value proposition

## Assets

Brand imagery and icons live under `assets/`. Update or replace `assets/icon.png` to adjust the favicon and inline header badge.
