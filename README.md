## Deliverables

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

 ###2A 


- **Lambda Function Name:** `sqs-image-generator`
- **SQS Queue ARN:** `arn:aws:sqs:eu-west-1:244530008913:image-generation-queue-cand83`

 - **SQS Queue URL**:  
  URL: [https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83](https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83)

###2B

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


####instruksjoner:
for å kjøre docker containeren

```bash

docker pull yousef1508/java-sqs-client:latest

docker run -e AWS_ACCESS_KEY_ID=<din-aws-access-key> \
           -e AWS_SECRET_ACCESS_KEY=<din-aws-secret-key> \
           -e SQS_QUEUE_URL=https://sqs.eu-west-1.amazonaws.com/244530008913/image-generation-queue-cand83 \
           yousef1508/java-sqs-client:latest "Din melding her"
```

---

## Task 4: Metrics and Monitoring

### Overview
Implemented **CloudWatch Alarm** to monitor SQS delays and send email alerts using **SNS**.

### Key Features
- **CloudWatch Alarm**: Triggers if the oldest message in the SQS queue exceeds the threshold (default: 300 seconds).
- **SNS Notifications**: Sends email alerts to the specified address (`sqs-alarm-cand83`).

### How to Test
1. Send a delayed message:
   ```bash
   aws sqs send-message --queue-url <queue-url> --message-body "Test" --delay-seconds 20
     ```