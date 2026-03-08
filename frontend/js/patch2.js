const fs = require('fs');
const file = 'c:\\Users\\nnyame\\Desktop\\Adamus KPI\\frontend\\js\\app.js';
let content = fs.readFileSync(file, 'utf8');

const newLogic = `    const updateOutlookVariance = () => {
        const outVal = parseFloat(outlook.input.value);
        const fcstVal = parseFloat(fullFcst.input.value);
        if (isNaN(outVal) || isNaN(fcstVal)) {
            budgVar.input.value = '';
            return;
        }
        let variance = 0;
        if (fcstVal === 0) {
            variance = outVal === 0 ? 0 : (outVal > 0 ? 100 : -100);
        } else {
            variance = ((outVal - fcstVal) / fcstVal) * 100;
        }
        if (variance > 100) variance = 100;
        if (variance < -100) variance = -100;
        budgVar.input.value = Math.round(variance) + '%';
    };
    outlook.input.addEventListener('input', updateOutlookVariance);
    fullFcst.input.addEventListener('input', updateOutlookVariance);`;

// Safety
content = content.replace(
    /    const updateSafetyOutlookVar = \(\) => \{\n        const val = parseFloat\(outlook\.input\.value\);\n        if \(isNaN\(val\)\) \{\n            budgVar\.input\.value = '';\n        \} else if \(val === 0\) \{\n            budgVar\.input\.value = '0%';\n        \} else if \(val > 0\) \{\n            budgVar\.input\.value = '-100%';\n        \}\n    \};\n    outlook\.input\.addEventListener\('input', updateSafetyOutlookVar\);/,
    newLogic
);

// Env
content = content.replace(
    /    \/\/ Custom logic for Outlook Variance \(Env Incidents\): 0 -> 0%, >0 -> -100%\n    outlook\.input\.addEventListener\('input', \(\) => updateEnvVariance\(outlook\.input, fullBudg\.input, budgVar\.input\)\);/,
    newLogic
);

// Prop Damage
content = content.replace(
    /    const updatePropDamOutlookVariance = \(\) => \{\n        budgVar\.input\.value = calculateVariance\(outlook\.input\.value, fullBudg\.input\.value, true\);\n    \};\n\n    outlook\.input\.addEventListener\('input', updatePropDamOutlookVariance\);\n    fullFcst\.input\.addEventListener\('input', updatePropDamOutlookVariance\);/,
    newLogic
);

fs.writeFileSync(file, content);
console.log("Patched successfully.");
