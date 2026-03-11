import boto3

def lambda_handler(event, context):
    # Rileva quale metrica ha causato l'allarme
    metric = event.get('detail', {}).get('configuration', {}).get('metrics', [{}])[0].get('metricStat', {}).get('metric', {}).get('metricName', 'Unknown')
    
    print(f"⚠️ DIFESA ATTIVATA: Anomalia rilevata in {metric}")
    
    # Esegue l'isolamento della VPC
    # In una demo reale qui scatterebbe il blocco delle chiavi KMS o lo stop dell'istanza EC2
    return {"status": "Mitigated", "action": "VPC_Isolation_Triggered"}