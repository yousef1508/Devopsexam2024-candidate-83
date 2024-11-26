### Versions and Dependencies

Below are the versions of tools and dependencies used in this project:

- **Terraform**: `v1.9.8`
- **AWS CLI**: `aws-cli/2.21.0 Python/3.12.6`
- **SAM CLI**: `1.112.0`
- **Python**: `3.9.16`
- **Git**: `2.40.1`
- **Operating System**:  
  `Linux ip-172-31-26-121.eu-west-1.compute.internal 6.1.112-124.190.amzn2023.x86_64 #1 SMP PREEMPT_DYNAMIC Wed Oct 23 06:32:04 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`



### Omfang og struktur

Oppgaven er holdt kort og konsis i henhold til retningslinjene gitt av professor Glenn Bech i en e-post sendt til kandidatene. Professoren understreket viktigheten av å fokusere på presis og klar fremstilling fremfor lange og detaljerte utredninger. Dette har blitt reflektert i hvordan oppgaven er strukturert og presentert.

---

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

<<<<<<< HEAD
 ### 2A 


- **Lambda Function Name:** `sqs-image-generator`
- **SQS Queue ARN:** `arn:aws:sqs:eu-west-1:244530008913:image-gen-queue-83`

 - **SQS Queue URL**:  
  URL: [https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-83](https://sqs.eu-west-1.amazonaws.com/244530008913/image-gen-queue-83))
=======
### Lambda and SQS Details
- **Lambda Function Name:** `sqs-image-generator`
- **SQS Queue ARN:** `arn:aws:sqs:eu-west-1:244530008913:image-generation-queue-cand83`
- **SQS Queue URL:**  
  [https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83](https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83)

>>>>>>> 0baeee1 (Readme update)

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


# Oppgave 5: Serverless, Function-as-a-Service vs. Container Technology

Implementering av systemer med serverløs arkitektur, som AWS Lambda og SQS, kontra en mer tradisjonell mikrotjenestearkitektur, er et omfattende tema. Begge tilnærmingene har sine styrker og svakheter, og det beste valget avhenger av det spesifikke brukstilfellet. Nedenfor analyseres disse arkitekturene basert på fire DevOps-prinsipper: Automatisering og CI/CD, Observabilitet, Skalerbarhet og kostnadskontroll, samt Eiendomsrett og ansvar.

## 1. **Automatisering og CI/CD**

- **Serverløs arkitektur**: Serverløse løsninger muliggjør effektiv distribusjon gjennom små, selvstendige funksjoner som kan implementeres raskt. Verktøy som Serverless Framework eller AWS SAM forenkler pakking og distribusjon, noe som fremmer automatisering. Imidlertid kan håndtering av mange små funksjoner introdusere kompleksitet, spesielt når det gjelder avhengigheter og vedlikehold av CI/CD-pipelines (ProDevOpsGuyTech, n.d.).

- **Mikrotjenestearkitektur**: Mikrotjenester benytter ofte containerisering (f.eks. Docker) og orkestrering (f.eks. Kubernetes), noe som kan gjøre CI/CD-prosessen mer omfattende. Dette krever mer innsats, men gir robust kontroll over hele kjeden fra bygging til distribusjon.

## 2. **Observabilitet (Overvåking)**

- **Serverløs arkitektur**: Overvåking og logging i serverløse miljøer kan være utfordrende på grunn av deres abstrakte natur. Verktøy som AWS CloudWatch er essensielle for innsikt, men "cold starts" kan være vanskelige å diagnostisere. Den distribuerte naturen krever effektiv bruk av sentralisert logging og sporingsverktøy for å oppnå oversikt (Lumigo, n.d.).

- **Mikrotjenestearkitektur**: Her er overvåking mer tradisjonell, med bruk av verktøy som Prometheus og Grafana for å samle inn metrikker. Utfordringen ligger i å aggregere logger fra ulike tjenester for å få en helhetlig forståelse av systemets tilstand.

## 3. **Skalerbarhet og kostnadskontroll**

- **Serverløs arkitektur**: Serverløse løsninger tilbyr automatisk skalering og en betalingsmodell basert på faktisk bruk, noe som er ideelt for applikasjoner med varierende trafikkmønstre. Imidlertid kan konstant høy trafikk føre til høyere kostnader sammenlignet med mikrotjenester (Enov8, n.d.).

- **Mikrotjenestearkitektur**: Gir mer kontroll over ressursallokering og kostnader. Skalerbarheten er solid, men krever manuell konfigurering og administrasjon for optimal ytelse og kostnadseffektivitet.

## 4. **Eiendomsrett og ansvar**

- **Serverløs arkitektur**: Skytilbyderen håndterer mye av infrastrukturen, noe som reduserer administrasjonsbyrden for utviklere. Dette gir mindre kontroll, og ved problemer må løsninger ofte tilpasses leverandørens rammer (MoldStud, n.d.).

- **Mikrotjenestearkitektur**: Gir full kontroll over infrastrukturen, men krever også at organisasjonen tar ansvar for alle aspekter av drift, inkludert pålitelighet og ytelse.

## Konklusjon

Valget mellom serverløs og mikrotjenestearkitektur avhenger av spesifikke behov og prioriteringer. Serverløse løsninger gir rask implementering og fleksibilitet, mens mikrotjenester tilbyr større kontroll og stabilitet. For applikasjoner med uforutsigbare arbeidsmengder eller strenge budsjettkrav kan serverløst være et godt valg. For mer komplekse applikasjoner som krever langvarig kontroll, kan mikrotjenester være mer passende.

## Referanser

- ProDevOpsGuyTech. (n.d.). *Serverless CI/CD: How to Build a Pipeline Without Servers*. Dev.to. Retrieved from [https://dev.to/prodevopsguytech/serverless-cicd-how-to-build-a-pipeline-without-servers-fn2](https://dev.to/prodevopsguytech/serverless-cicd-how-to-build-a-pipeline-without-servers-fn2)
- Lumigo. (n.d.). *Microservices Observability: 3 Pillars and 6 Patterns*. Lumigo. Retrieved from [https://lumigo.io/microservices-monitoring/microservices-observability](https://lumigo.io/microservices-monitoring/microservices-observability)
- Enov8. (n.d.). *Serverless Architectures: Benefits and Challenges*. Enov8. Retrieved from [https://www.enov8.com/blog/serverless-architectures-benefits-and-challenges](https://www.enov8.com/blog/serverless-architectures-benefits-and-challenges)
- MoldStud. (n.d.). *Serverless in the Enterprise: Challenges and Solutions for Large-Scale Deployment*. MoldStud. Retrieved from [https://moldstud.com/articles/p-serverless-in-the-enterprise-challenges-and-solutions-for-large-scale-deployment](https://moldstud.com/articles/p-serverless-in-the-enterprise-challenges-and-solutions-for-large-scale-deployment)
