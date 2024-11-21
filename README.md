# Oppsummering av Leveranser for Oppgave 1 (SAM + API Gateway)

## Implementerte Funksjoner:
- **Lambda-funksjon**: Tar imot input fra API Gateway og laster opp til S3.
- **POST API-endepunkt**: Konfigurert og testet ved bruk av `/generate`.
- **SAM-deployment**: Verifisert og funksjonell.

## Oppgave 1A:
- **API Gateway URL**:  
https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/


- **Eksempel på S3-filbane**:  
s3://pgr301-couch-explorers/83/<unikt-filnavn>.txt
Eller bruk en faktisk filsti fra eksisterende filer i bucketen, denne har jeg allerede generert for eksempel:  
s3://pgr301-couch-explorers/83/06148839-6bd5-4dbc-8dae-fc8697732dba.txt
har testet sam Local invoke (I build fasen før deploy), Curl (etter sam Deploy --guided) og Postman

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