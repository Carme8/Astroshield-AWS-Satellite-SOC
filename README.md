# 🛰️ AstroShield: AWS Satellite Security Operations Center (SOC)

**Astro-Shield** è un framework di simulazione avanzato per la protezione delle infrastrutture critiche spaziali (**Ground Segment**). Il progetto dimostra come implementare una pipeline di ricezione dati satellitari sicura utilizzando un'architettura **Zero Trust**, crittografia granulare e analisi forense automatizzata.

---

## 🛡️ Security Features

### 1. Data Integrity & WORM Storage
I dati ricevuti in banda X vengono archiviati in un vault **Amazon S3** con policy **Object Lock** (WORM - Write Once, Read Many).
* **Difesa:** Previene il Data Tampering e i Ransomware. Anche un attaccante con permessi di admin non può alterare la telemetria storica.
* **Compliance:** Risponde ai requisiti della direttiva **NIS2** per la conservazione integra dei dati critici.

### 2. Orbital Forensic Engine (AI-Driven)
Monitoraggio in tempo reale del flusso **VITA-49.2** per identificare anomalie comportamentali tramite **AWS Lambda** e **GuardDuty**.
* **Signal Hijacking Detection:** Rilevamento di picchi anomali nel consumo energetico (RF Power) o deviazioni nei parametri orbitali (TLE).
* **Automated Response:** Isolamento immediato della rete (**VPC Isolation**) in caso di firma di attacco rilevata.

### 3. Infrastructure as Code (IaC) & Zero Trust
* **Crittografia:** Ogni pacchetto è cifrato a riposo con chiavi **AES-256** gestite tramite **AWS KMS**.
* **Least Privilege:** Policy IAM granulari limitano l'accesso ai soli microservizi necessari, eliminando ogni punto di ingresso non autorizzato.

---

## 🏗️ System Architecture & Data Flow

![AstroShield_System_Architecture](https://github.com/user-attachments/assets/08e9d017-7243-47fd-b727-a3e0780bee9c)

| Componente | Descrizione e Ruolo di Sicurezza | Flusso Dati |
| :--- | :--- | :--- |
| **🛰️ Satellite SNPP** | Segmento spaziale simulato che genera telemetria mission-critical. | Invia segnale RF (simulato). |
| **📡 AWS Ground Station** | Punto di ingresso gestito. Isola RF dalla rete IP. | Converte in stream VITA-49.2/UDP. |
| **☁️ Amazon VPC** | Ambiente isolato. Ingresso dati tramite ENI dedicata. | Instrada pacchetti verso EC2. |
| **🖥️ Amazon EC2** | Istanza Hardened (SDR). Software Amphinicy Blink. | Elabora e salva su S3. |
| **🗄️ Amazon S3** | Vault finale con **Object Lock** (Compliance Mode). | Impedisce il Data Tampering (WORM). |

---

## 🎬 Demo Scripts: Astro-Shield in Azione

### Scena 1: Stato Nominale (Green Zone)
In questa fase, la pipeline riceve dati in Banda X. Il segnale è autentico e i controlli di integrità sono superati.
* **Dashboard:** Power Consumption stabile, Orbital Drift ~0.001°, Rischio Basso.



https://github.com/user-attachments/assets/588707e7-d7ad-40b1-892e-e08336946bfa



### Scena 2: Rilevamento Attacco (Red Zone)
Il sistema rileva un tentativo di hijacking orbitale tramite un picco anomalo di potenza (Power Spike).
* **Dashboard:** Alert visivo rosso, rischio al 68%, log: `UNAUTHORIZED MANEUVER ATTEMPT DETECTED`.

<img width="1917" height="997" alt="Anomaly_Detection_Power_Spike" src="https://github.com/user-attachments/assets/44decd2f-5643-47bc-8bd0-ac46e38f97cb" />

### Scena 3: Risposta Automatica (Mitigation)
La Lambda "Trigger Defense" isola l'istanza SDR e revoca le chiavi KMS. Il dato originale è salvo nel vault S3.

https://github.com/user-attachments/assets/41a56c3b-e926-4d1c-8b4a-f1b454e671e8

**Log di Backend:**

<img width="1915" height="634" alt="Backend_Telemetry_Logs" src="https://github.com/user-attachments/assets/92532363-160c-4baf-b0eb-c8e255d753ab" />

---

## 🛠️ Tech Stack
* **Cloud:** AWS (Ground Station, S3, Lambda, GuardDuty, KMS, CloudWatch)
* **IaC:** Python CDK
* **SDR Engine:** Amphinicy Blink (Simulato)
* **Frontend:** HTML5/CSS3 (Mission Control Dashboard)
* **Backend/Bridge:** Python Flask & Boto3
* **Simulation:** Docker, LocalStack (Local Cloud Environment)

<img width="1919" height="1030" alt="Data_Immutability_S3_ObjectLock" src="https://github.com/user-attachments/assets/079df7ed-3a62-4aee-8303-dec3330b814e" />

---

## 💰 Cost Analysis (Estimated)
| Servizio | Voce di Costo | Stima Mensile | Note |
| :--- | :--- | :--- | :--- |
| **AWS Ground Station** | Prenotazione Antenna | ~$10 - $20 | Basato su "Reserved contacts". |
| **Amazon EC2** | Istanza t3.medium | ~$30 | Free Tier eligible (t2/t3 micro). |
| **S3 & Lambda** | Storage + Forensics | < $2 | Costi minimi per volumi demo. |

---
## 💻 How to Run

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/tuo-username/AstroShield-SOC.git](https://github.com/tuo-username/AstroShield-SOC.git)
2. **Start the Telemetry Bridge:**
   ```bash
   python bridge.py
3. **Launch Dashboard:**
   ```bash
   Apri index.html nel browser
   ```

---

*Disclaimer
Questo progetto ha scopi puramente educativi e di ricerca nel campo della Space Cybersecurity. Non è destinato all'uso in ambienti di produzione senza una revisione completa dei protocolli di sicurezza RF reali.*

@ AWS AstroShield 2026
