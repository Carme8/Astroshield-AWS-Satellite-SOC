from flask import Flask, jsonify
from flask_cors import CORS
import boto3
import datetime
import random

app = Flask(__name__)
CORS(app)

# Connessione a LocalStack
cw = boto3.client('cloudwatch', endpoint_url="http://localhost:4566", region_name='eu-central-1')

@app.route('/stats')
def get_stats():
    try:
        # Cerchiamo di prendere i dati reali da CloudWatch
        now = datetime.datetime.utcnow()
        start = now - datetime.timedelta(seconds=60)
        
        res = cw.get_metric_statistics(
            Namespace='SatelliteSecurity',
            MetricName='RF_Power',
            StartTime=start,
            EndTime=now,
            Period=60,
            Statistics=['Average']
        )
        
        datapoints = res.get('Datapoints', [])
        if datapoints:
            rf_val = round(datapoints[-1]['Average'], 2)
        else:
            # Se CloudWatch è ancora vuoto, mandiamo un dato simulato per non bloccare l'HTML
            rf_val = round(random.uniform(110, 140), 2)
            
        is_attack = rf_val > 300
        
        return jsonify({
            "rf_power": rf_val,
            "orbital_drift": 0.002,
            "is_attack": is_attack
        })
    except Exception as e:
        print(f"Errore Bridge: {e}")
        return jsonify({"rf_power": "ERR", "is_attack": False})

if __name__ == '__main__':
    print("✅ Bridge Astro-Shield pronto su http://localhost:5000")
    app.run(port=5000)