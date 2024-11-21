# Oppsummering av Leveranser for Oppgave 1 (SAM + API Gateway)

## Implementerte Funksjoner:
- **Lambda-funksjon**: Tar imot input fra API Gateway og laster opp til S3.
- **POST API-endepunkt**: Konfigurert og testet ved bruk av `/generate`.
- **SAM-deployment**: Verifisert og funksjonell.

## Oppgave 1A:
Oppgave 1A: Dokumentasjon
API Gateway URL:
**https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/**

Eksempel på Payload (POST):


{
    "prompt": "Test content generation"
}

**Eksempel på S3-filbane:**


s3://pgr301-couch-explorers/83/<unikt-filnavn>.txt 


**Eksempel fra testing:**


**s3://pgr301-couch-explorers/83/2352ef88-ced6-4d44-b08f-0c3e5d95de3d.txt**

**Testmetoder brukt:**

SAM Local: Verifisert under build-fasen (sam local invoke) med event-payloads.
cURL: Testet API Gateway etter deployment.
Postman: Testet API-funksjonalitet med JSON-payload.


## Oppgave 1B: GitHub Actions Workflow
GitHub Actions for Deployment:
Workflow-filen (.github/workflows/deploy_lambda.yml) håndterer automatisk bygging og deployering av Lambda-funksjonen ved bruk av AWS SAM CLI. Deployment trigges automatisk ved hver commit til main-grenen.

**AWS Credentials:**
AWS Access Key ID og Secret Access Key er konfigurert som hemmeligheter i GitHub (AWS_ACCESS_KEY_ID og AWS_SECRET_ACCESS_KEY) for sikker tilgang.

**Beskrivelse av Workflow:**

Installer Python og SAM CLI: Sikrer at nødvendig miljø er satt opp.
Bygg SAM-applikasjonen: Kjører sam build for å forberede funksjonen.
Deploy SAM-applikasjonen: Kjører sam deploy --no-confirm-changeset for å oppdatere Lambda-funksjonen i skyen.
Filbane for Workflow:

.github/workflows/deploy_lambda.yml
**Trigger:**
Workflow trigges automatisk ved push til main-grenen.

**Lenke til vellyket kjørt GitHub Actions workflow:**
https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11946931320