import urllib.request
import json

url = "http://127.0.0.1:8000/api/kpi/Engineering"

try:
    with urllib.request.urlopen(url) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(f"Total records fetched: {len(data)}")
            
            fixed_inputs = [r for r in data if r.get('subtype') == 'fixed_input']
            print(f"Fixed Input records found: {len(fixed_inputs)}")
            
            prime_excavators = [r for r in fixed_inputs if r.get('metric_name') == 'Prime Excavators']
            print(f"Prime Excavators Fixed Inputs found: {len(prime_excavators)}")
            
            for r in prime_excavators:
                print(f"Date: {r.get('date')}, Data: {r.get('data')}")
        else:
            print(f"Error: {response.status}")

except Exception as e:
    print(f"Exception: {e}")
