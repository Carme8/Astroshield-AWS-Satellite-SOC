import boto3
import time
import random

# Configurazione LocalStack
ENDPOINT = "http://localhost:4566"
cw = boto3.client('cloudwatch', 
                  endpoint_url=ENDPOINT, 
                  region_name='eu-central-1',
                  aws_access_key_id='test', 
                  aws_secret_access_key='test')

def run_simulation():
    print("🛰️ Astro-Shield: Simulatore SNPP attivo...")
    while True:
        is_attack = random.random() < 0.15
        rf_power = round(random.uniform(400, 600) if is_attack else random.uniform(110, 140), 2)
        
        try:
            cw.put_metric_data(
                Namespace='SatelliteSecurity',
                MetricData=[
                    {'MetricName': 'RF_Power', 'Value': rf_power, 'Unit': 'None'},
                    {'MetricName': 'Attack_Flag', 'Value': 1 if is_attack else 0, 'Unit': 'None'}
                ]
            )
            print(f"[{time.strftime('%H:%M:%S')}] Inviato: {rf_power}W | Attacco: {is_attack}")
        except Exception as e:
            print(f"Errore: {e}")
            
        time.sleep(2)

if __name__ == "__main__":
    run_simulation()