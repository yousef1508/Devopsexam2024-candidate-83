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