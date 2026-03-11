# 🛰️ AstroShield: AWS Satellite Security Operations Center (SOC)

**AstroShield** è una piattaforma di monitoraggio avanzata progettata per simulare un Security Operations Center (SOC) dedicato alle infrastrutture spaziali. Il sistema dimostra come l'integrazione tra telemetria satellitare in tempo reale e servizi Cloud AWS possa identificare e mitigare minacce critiche come il **RF Jamming**.

---

## 🚀 Key Features

* **Real-Time Telemetry Bridge:** Monitoraggio dinamico di potenza RF e deviazione orbitale TLE tramite WebSocket/Flask.
* **Intelligent Threat Detection:** Simulazione di **Amazon GuardDuty** per l'analisi comportamentale del segnale.
* **Visual Signal Analytics:** * *Waterfall Spectrogram:* Visualizzazione dinamica dello spettro di frequenza.
    * *Anomaly Waveforms:* Grafici reattivi che mutano colore e frequenza durante gli incidenti.
* **Data Integrity Enforcement:** Concetti di **S3 Object Lock** e cifratura **KMS** per garantire l'immutabilità dei dati ricevuti.
* **Incident Response UI:** Dashboard ad alto contrasto con allerta visiva immediata per minacce ad alta severità.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Canvas API per rendering spettrografico).
* **Backend:** Python 3 + Flask (Telemetria e simulazione attacchi).
* **Security Architecture:** Ispirato al AWS Well-Architected Framework.

---

## 🏗️ System Architecture

Il progetto simula un'infrastruttura Ground-to-Cloud completa:
1. **Ingest:** Segnale simulato dal backend Python.
2. **Processing:** Il Bridge invia i dati alla dashboard via API.
3. **Monitoring:** Analisi dei picchi di potenza per attivare i trigger di sicurezza.
4. **Protection:** Simulazione del blocco dei dati su storage immutabile.

![Architecture Diagram](AstroShield_System_Architecture.jpg)

---

## 🚨 Incident Response Simulation

### 🟢 Nominal State
In condizioni normali, il sistema monitora un segnale pulito. La telemetria è stabile e il waterfall mostra una distribuzione di frequenza coerente.
*(Video di riferimento: `Mission_Control_Nominal_State.mp4`)*

### 🔴 Under Attack (RF Jamming)
Al rilevamento di un'interferenza intenzionale:
1. Il sistema vira in **Red Alert Mode**.
2. L'alert **"HIGH SEVERITY: RF JAMMING DETECTED"** appare istantaneamente.
3. Il waterfall mostra saturazione del canale (rumore rosso).

![Incident Alert](Screenshot%202026-03-11%20112227.jpg)

---

## 💻 How to Run

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/tuo-username/AstroShield-SOC.git](https://github.com/tuo-username/AstroShield-SOC.git)
