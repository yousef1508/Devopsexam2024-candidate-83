## Leveranser:

### Oppgave 1

 ### 1A

- **HTTP Endpoint for Lambda Function:**  
  URL: [https://j983bpau2h.execute-api.eu-west-1.amazonaws.com/Prod/generate](https://j983bpau2h.execute-api.eu-west-1.amazonaws.com/Prod/generate)

### 1B

- **GitHub Actions Workflow Run:**  
  [![GitHub Actions Workflow](https://img.shields.io/badge/GitHub-Actions--Workflow-blue)](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11965900101/job/33360682266)  
  URL: [https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11965900101/job/33360682266](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11965900101/job/33360682266)


### Eksempel på forespørsel
For å teste HTTP-endepunktet kan du bruke følgende eksempel i Postman eller `curl`:

**Prompt:**
```json
{
  "prompt": "Place me in a jeep on an African savanna with lions and elephants in the background under a golden sunset."
}
```

---

### Oppgave 2

 ### 2A 


- **Lambda Function Name:** `sqs-image-generator`
- **SQS Queue ARN:** `arn:aws:sqs:eu-west-1:244530008913:image-gen-queue-83`

 - **SQS Queue URL**:  
  URL: [https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-83](https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-83))

### 2B

- **Link til en vellykket GitHub Actions workflow (Main Branch):**  

  [![GitHub Actions Workflow - Main Branch](https://img.shields.io/badge/GitHub-Actions--Workflow--Main-brightgreen)](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986740646)  
  
  URL: [https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986740646](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986740646)

- **Link til en vellykket GitHub Actions workflow (Ikke-main Branch):**

 [![GitHub Actions Workflow - Non-Main Branch](https://img.shields.io/badge/GitHub-Actions--Workflow--Non--Main-brightgreen)](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986726072)  
 
  URL: [https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986726072](https://github.com/yousef1508/Devopsexam2024Yoas001/actions/runs/11986726072)
  


---

### Oppgave 3

### 3A: Lage en docker fil

Dockerfilen bruker en flertrinns strategi:
bygger appen med Maven og lager et kompakt kjøretidsbilde med (`eclipse-temurin:17-jre`)
Dette sikrer at det er kompakt og effektivit. 

### 3B: Publish Docker Image to Docker Hub
Jeg valgte å bruke latest-taggen for Docker-imaget. 
Grunnen er ganske enkel: det gjør alt mye mer praktisk. 
Når noen trekker ned imaget fra Docker Hub, får de alltid den nyeste og mest oppdaterte versjonen uten å måtte bekymre seg for detaljer. hvis det er behov for flere versjoner eller sikre kompatibilitet,
kunne jeg ha lagt til spesifikke versjonstags.
Men akkurat nå fungerer det best å holde det enkelt og oversiktlig, som samt svarer på 3b fullt fra mitt perspektiv.


**Contianer Image name og Sqs url**
container Image name

`yousef1508/java-sqs-client`

- **SQS Queue URL:**  
  [https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83](https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83)


#### instruksjoner:
for å kjøre docker containeren

```bash

docker pull yousef1508/java-sqs-client:latest

docker run -e AWS_ACCESS_KEY_ID=<din-aws-access-key> \
           -e AWS_SECRET_ACCESS_KEY=<din-aws-secret-key> \
           -e SQS_QUEUE_URL=https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83 \
           yousef1508/java-sqs-client:latest "Din melding her"
```

---

## Oppgave 4: monitoring og overvåking

### Oversikt
Implementert **CloudWatch Alarm** for å overvåke SQS-forsinkelser og sende e-postvarsler ved hjelp av **SNS**.

### Nøkkelfunksjoner
- **CloudWatch Alarm**: Utløses hvis den eldste meldingen i SQS-køen overskrider terskelen.
- **SNS-Notifications**: Sender e-postvarsler til den angitte adressen (i sns topicen `sqs-alarm-cand83`).

### Hvordan teste
1. slå av lambda funksjonen midlertidig og Send en vanlig eller en delayed melding over thresholden:
   ```bash
    aws sqs send-message --queue-url https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83 --message-body "Delayed Test Message" --delay-seconds 68 
    ```

---


### Oppgave 5: Serverless, Function-as-a-Service vs. Container Technology

Implementering av systemer med serverløs arkitektur, som AWS Lambda og SQS, kontra en mer tradisjonell mikrotjenestearkitektur, er et ganske heftig tema. Begge tilnærmingene har styrker og svakheter, og hva som fungerer best kommer helt an på brukstilfellet. Her skal jeg bryte det ned basert på fire DevOps-prinsipper: Automatisering og CI/CD, Observabilitet, Skalerbarhet og kostnadskontroll, og til slutt Eiendomsrett og ansvar.

#### 1. **Automatisering og CI/CD**
- **Serverløs arkitektur**
 Serverløse løsninger gjør distribusjon vanvittig effektivt. Her snakker vi om små, selvstendige funksjoner som kan pushes til skyen på sekunder. Det blir som å ha en pipeline som er trimmet for Formel 1-løp. Verktøy som Serverless Framework eller AWS SAM tar seg av det meste av pakking og deploy, og de er nesten som magi når det gjelder automatisering. Men – og dette er et stort men – hvis du har hundrevis av små funksjoner, kan det føles som å holde styr på 100 spinnville katter. Avhengigheter må håndteres, og pipelines må være vanntette for å unngå kaos.

- **Mikrotjenestearkitektur**
Mikrotjenester er derimot litt som tunge maskiner – større og kraftigere, men ikke like lette å flytte rundt. Her er CI/CD litt mer omfattende fordi containerisering (tenk Docker) og orkestrering (Kubernetes) er standarden. Det krever mer innsats, men til gjengjeld får du robust kontroll over hele kjeden fra bygg til deploy.

#### 2. **Observabilitet (Overvåking)**
- **Serverløs arkitektur**
Dette er kanskje der serverløst virkelig utfordrer deg. Overvåking og logging er som å jobbe med en usynlig fiende. Alt er abstrakt. Du er helt avhengig av verktøy som AWS CloudWatch for innsikt, og "cold starts" kan være en pest og plage å diagnostisere.

Den distribuerte naturen gjør feilsøking litt som å lete etter en nål i en høystakk. Du må virkelig ha styr på sentralisert logging og trace-verktøy for å få overblikk.

- **Mikrotjenestearkitektur**
Her er overvåkingsspillet litt mer tradisjonelt. Du kan bruke Prometheus, Grafana, eller lignende verktøy til å hente metrikker og holde oversikt over alt. Kompleksiteten ligger i å samle logger fra alle tjenestene og sette dem sammen til noe meningsfullt. Men det er i det minste en kjent utfordring.

#### 3. **Skalerbarhet og kostnadskontroll**
- **Serverløs arkitektur**
Hvis vi snakker om elastisitet, er serverløst uslåelig. Det skalerer opp og ned som en drøm uten at du trenger å røre en finger. Og kostnadene? Du betaler kun for hva du bruker. Hvis trafikken din er ujevn, er dette gull.

Men – og dette er viktig – hvis du har konstant høy trafikk, kan det bli dyrere enn mikrotjenester. Kostnad per kall kan virkelig samle seg opp.

- **Mikrotjenestearkitektur**
Her har du mer kontroll. Du kan provisionere nøyaktig hvor mye du trenger og optimalisere ressursene. Skalerbarheten er også solid, men den krever at du holder på med konfigurering og administrasjon. Det er som en manuelt justert motor: kraftig, men arbeidskrevende.

#### 4. **Eiendomsrett og ansvar**
- **Serverløs arkitektur**
Her ligger mye av ansvaret hos skytilbyderen. Du skriver kode, de tar seg av resten. Det er mindre å bekymre seg for, men også mindre kontroll. Hvis det går galt, er det som regel du som må finne løsningen på skyens premisser.

- **Mikrotjenestearkitektur**
Alt er ditt ansvar. Dette kan være både bra og dårlig. Du har full kontroll, men det betyr også at du må holde alt i gang, fra infrastruktur til pålitelighet og ytelse.

### Konklusjon
Valget mellom serverløst og mikrotjenester handler om prioriteringer. Serverløst gir deg fart og fleksibilitet, mens mikrotjenester gir deg kontroll og stabilitet. For applikasjoner med uforutsigbare arbeidsmengder eller strenge budsjettkrav kan serverløst være et fantastisk valg. Men hvis du trenger langvarig kontroll og kompleks funksjonalitet, er mikrotjenester kanskje mer din greie.

