# DevOps Eksamen - Lambda Innholds Generator

Dette prosjektet implementerer en serverløs applikasjon ved bruk av AWS SAM (Serverless Application Model) for å lage et API Gateway-endepunkt og en Lambda-funksjon som genererer innhold basert på en brukerdefinert forespørsel og laster det opp til en S3-bucket.

---

## Prosjektoversikt

Systemet består av:
- **Lambda-funksjon**: Behandler `POST`-forespørsler, genererer innhold og laster det opp til S3.
- **API Gateway**: Tilbyr `/generate`-endepunktet for å sende forespørsler til Lambda-funksjonen.
- **S3 Bucket**: Lagrer det genererte innholdet i formatet `s3://pgr301-couch-explorers/83/<unik-filnavn>.txt`.

---

## API Detaljer

### **POST /generate**
- **Endepunkt**: 
https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/



- **Forespørsel Payload**:
```json
{
  "prompt": "Innhold her"
}
Respons Eksempel:
json

{
  "message": "File Successfully uploaded",
  "file_key": "83/bd2de50f-be1d-48ce-9892-4a75ba5a7e55.txt"
}
Hvordan teste
Ved bruk av curl:


curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Test generering av innhold"}' https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/
Ved bruk av Postman:
Opprett en ny forespørsel i Postman.
Sett metoden til POST.
Legg inn endepunkt-URL:


https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/
I Body-fanen, velg raw og sett format til JSON. Legg til payload:
json

{
  "prompt": "Test generering av innhold"
}
Send forespørselen og sjekk responsen.
S3 Bucket Informasjon
Bucket Navn: pgr301-couch-explorers
Eksempel Filsti:


s3://pgr301-couch-explorers/83/bd2de50f-be1d-48ce-9892-4a75ba5a7e55.txt
For å vise filinnholdet:
Last ned filen via AWS-konsollen.
Eller, ved bruk av AWS CLI:


aws s3 cp s3://pgr301-couch-explorers/83/bd2de50f-be1d-48ce-9892-4a75ba5a7e55.txt .
cat bd2de50f-be1d-48ce-9892-4a75ba5a7e55.txt
Prosjektstruktur




Bygg applikasjonen:



sam build
Distribuer applikasjonen:



sam deploy --guided
Bruk følgende parametere under distribusjonen:

Stack Name: sam-lambda-stack-83
Region: eu-west-1
Resultater: Etter distribusjon vil følgende resultater bli gitt:

API Gateway Endepunkt:


https://aj9pvletme.execute-api.eu-west-1.amazonaws.com/Prod/generate/
Lambda Funksjon ARN:
ruby

arn:aws:lambda:eu-west-1:244530008913:function:sam-lambda-stack-83-HelloWorldFunction
Repository
GitHub Repository: 
Takk
Dette prosjektet ble laget for PGR301 Couch Explorers DevOps Eksamen.
Kandidatnummer: 83.