// Handling for Ore Mined
if (STATE.currentMetric === 'Ore Mined') {
    filteredRecords = records.filter(r => r.metric_name === STATE.currentMetric && r.subtype !== 'fixed_input');

    // Date | Daily Actual | Daily Forecast | Daily Var % | MTD Actual | MTD Forecast | MTD Var % | Outlook (a) | Full Forecast (b) | Full Budget (c) | Budget Var % | Action
    thead.innerHTML = `
                <th style="padding: 12px; text-align: left; min-width: 90px;">Date</th>
                <th style="padding: 12px; text-align: left;">Daily Actual</th>
                <th style="padding: 12px; text-align: left;">Daily Forecast</th>
                <th style="padding: 12px; text-align: left;">Daily Var %</th>
                <th style="padding: 12px; text-align: left;">MTD Actual</th>
                <th style="padding: 12px; text-align: left;">MTD Forecast</th>
                <th style="padding: 12px; text-align: left;">MTD Var %</th>
                <th style="padding: 12px; text-align: left;">Outlook (a)</th>
                <th style="padding: 12px; text-align: left;">Full Forecast (b)</th>
                <th style="padding: 12px; text-align: left;">Full Budget (c)</th>
                <th style="padding: 12px; text-align: left;">Budget Var %</th>
                <th style="padding: 12px; text-align: left;">Action</th>
            `;

    if (filteredRecords.length === 0) {
        tbody.innerHTML = `<tr><td colspan="12" style="padding: 12px; text-align: center;">No records found for ${STATE.currentMetric}</td></tr>`;
        return;
    }

    filteredRecords.forEach(r => {
        const tr = document.createElement('tr');
        tr.style.borderTop = '1px solid #e5e7eb';

        let dateDisplay = r.date;
        if (r.date && r.date.includes('-')) {
            const [y, m, d] = r.date.split('-');
            dateDisplay = `${d}-${m}-${y}`;
        }

        const val = (v) => (v !== undefined && v !== null && v !== '') ? v : '-';

        tr.innerHTML = `
                    <td style="padding: 12px;">${dateDisplay}</td>
                    <td style="padding: 12px;">${val(r.data.daily_actual)}</td>
                    <td style="padding: 12px;">${val(r.data.daily_forecast)}</td>
                    <td style="padding: 12px;">${val(r.data.var1)}</td>
                    <td style="padding: 12px;">${val(r.data.mtd_actual)}</td>
                    <td style="padding: 12px;">${val(r.data.mtd_forecast)}</td>
                    <td style="padding: 12px;">${val(r.data.var2)}</td>
                    <td style="padding: 12px;">${val(r.data.outlook)}</td>
                    <td style="padding: 12px;">${val(r.data.full_forecast)}</td>
                    <td style="padding: 12px;">${val(r.data.full_budget)}</td>
                    <td style="padding: 12px;">${val(r.data.var3)}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>
                        <button onclick="deleteRecord(${r.id})" style="padding:2px 6px; cursor:pointer; color:red;" title="Delete">🗑️</button>
                    </td>
                `;
        tbody.appendChild(tr);
    });
    return;
}

