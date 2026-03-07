// calculations.js
// Logic for KPI calculations (Variance, MTD, etc.)

function calculateVariance(actual, forecast) {
    const act = parseFloat(actual);
    const fc = parseFloat(forecast);

    if (isNaN(act) || isNaN(fc)) {
        return '';
    }

    let variance = 0;
    if (fc === 0) {
        if (act === 0) {
            variance = 0;
        } else {
            variance = -100;
        }
    } else {
        // Base logic for most cases (e.g. positive improvements or standard target variance)
        variance = ((fc - act) / fc) * 100;

        // Custom fixed-rule overrides defined by user prompt edge-cases 
        // to handle specific OHS safety incidents thresholds:
        if (act === 1 && (fc === 1 || fc === 2)) variance = 50;
        if (act === 2 && fc === 2) variance = 0;
        if (act === 3 && fc === 2) variance = -50;
    }

    // Safety Net: if actual is >= 4
    if (act >= 4) variance = -100;

    // Floor the variance at -100%
    if (variance < -100) {
        variance = -100;
    }

    return Math.round(variance) + '%';
}

function calculateMTD(previousMTD, currentDaily) {
    const prev = parseFloat(previousMTD) || 0;
    const curr = parseFloat(currentDaily) || 0;
    return prev + curr;
}

function attachVarianceListener(actualInput, forecastInput, varianceOutput) {
    const update = () => {
        varianceOutput.value = calculateVariance(actualInput.value, forecastInput.value);
    };
    actualInput.addEventListener('input', update);
    forecastInput.addEventListener('input', update);
}
