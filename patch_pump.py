import sys
import re

file_path = r"c:\Users\nnyame\Desktop\Adamus KPI\frontend\js\app.js"
with open(file_path, 'r', encoding='utf-8') as f:
    in_text = f.read()

# Normalize newlines
in_text = in_text.replace('\r\n', '\n')

# 1. Update DEPT_METRICS
in_text = in_text.replace(
'''        "Graders",
        "Dozers",
        "Drill Rigs",
        "Crusher",
        "Mill"''', 
'''        "Graders",
        "Dozers",
        "Drill Rigs",
        "Dewatering Pumps",
        "Crusher",
        "Mill"'''
)

# 2. Update condition line 1198
in_text = in_text.replace(
'''        } else if ((metric === "Light Vehicles" || metric === "Tipper Trucks" || metric === "Prime Excavators" || metric === "Anx Excavators" || metric === "Dump Trucks" || metric === "ART Dump Trucks" || metric === "Wheel Loaders" || metric === "Graders" || metric === "Dozers" || metric === "Drill Rigs") && STATE.currentDept === "Engineering") {''',
'''        } else if ((metric === "Light Vehicles" || metric === "Tipper Trucks" || metric === "Prime Excavators" || metric === "Anx Excavators" || metric === "Dump Trucks" || metric === "ART Dump Trucks" || metric === "Wheel Loaders" || metric === "Graders" || metric === "Dozers" || metric === "Drill Rigs" || metric === "Dewatering Pumps") && STATE.currentDept === "Engineering") {'''
)

# 3. Update Line 1342
in_text = in_text.replace(
'''    } else if (dept === "Engineering" && metricName === "Drill Rigs") {
        renderEngineeringDrillRigsForm(dept, metricName, card);
    } else if (dept === "Engineering" && metricName === "Crusher") {''',
'''    } else if (dept === "Engineering" && metricName === "Drill Rigs") {
        renderEngineeringDrillRigsForm(dept, metricName, card);
    } else if (dept === "Engineering" && metricName === "Dewatering Pumps") {
        renderEngineeringDewateringPumpsForm(dept, metricName, card);
    } else if (dept === "Engineering" && metricName === "Crusher") {'''
)

# 4. Update table rendering condition line 9516
in_text = in_text.replace(
    '''if (STATE.currentMetric === 'Anx Excavators' || STATE.currentMetric === 'Dump Trucks' || STATE.currentMetric === 'ART Dump Trucks' || STATE.currentMetric === 'Wheel Loaders' || STATE.currentMetric === 'Dozers' || STATE.currentMetric === 'Graders' || STATE.currentMetric === 'Drill Rigs') {''',
    '''if (STATE.currentMetric === 'Anx Excavators' || STATE.currentMetric === 'Dump Trucks' || STATE.currentMetric === 'ART Dump Trucks' || STATE.currentMetric === 'Wheel Loaders' || STATE.currentMetric === 'Dozers' || STATE.currentMetric === 'Graders' || STATE.currentMetric === 'Drill Rigs' || STATE.currentMetric === 'Dewatering Pumps') {'''
)

# 5. Extract renderEngineeringDrillRigsForm and duplicate
start_str = "function renderEngineeringDrillRigsForm(dept, metricName, card) {"
end_str = "function renderEngineeringCrusherForm(dept, metricName, card) {"

start_idx = in_text.find(start_str)
end_idx = in_text.find(end_str, start_idx)

if start_idx != -1 and end_idx != -1:
    orig_func = in_text[start_idx:end_idx]
    new_func = orig_func.replace("DrillRigs", "DewateringPumps").replace("Drill Rigs", "Dewatering Pumps")
    
    in_text = in_text[:end_idx] + new_func + in_text[end_idx:]
else:
    print("Function not found!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(in_text)

print("Done")
