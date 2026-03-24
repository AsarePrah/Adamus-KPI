import sys

file_path = r"c:\Users\nnyame\Desktop\Adamus KPI\frontend\js\app.js"
with open(file_path, 'r', encoding='utf-8') as f:
    in_text = f.read()

in_text = in_text.replace('\r\n', '\n')

# 1. renderCrushingGradeForm variables
in_text = in_text.replace(
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);''',
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);

    const day2 = DOM.createInputGroup("Day-2", `input-${dept}-day2`, "number");'''
)

# 2. renderCrushingGradeForm logic
in_text = in_text.replace(
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }
        } catch (e) {
            console.error("Error fetching fixed inputs", e);
        }
    };
    date.input.addEventListener('change', fetchFixedInputs);''',
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }

            // Calculate Day-2 Value
            if (d.getDate() === 1) {
                day2.input.value = 0;
            } else {
                const prevDate = new Date(d);
                prevDate.setDate(d.getDate() - 1);
                const pY = prevDate.getFullYear();
                const pM = String(prevDate.getMonth() + 1).padStart(2, '0');
                const pD = String(prevDate.getDate()).padStart(2, '0');
                const prevDateStr = f"{pY}-{pM}-{pD}";
                const prevRecord = records.find(r => r.metric_name === metricName && r.subtype !== 'fixed_input' && r.date === prevDateStr);
                if (prevRecord && prevRecord.data) {
                    day2.input.value = prevRecord.data.daily_actual || 0;
                } else {
                    day2.input.value = 0;
                }
            }
        } catch (e) {
            console.error("Error fetching fixed inputs", e);
        }
    };
    date.input.addEventListener('change', fetchFixedInputs);'''
)

# fix f-string issue in raw javascript:
in_text = in_text.replace('f"{pY}-{pM}-{pD}"', '`${pY}-${pM}-${pD}`')

# 3. renderCrushingGradeForm grid
in_text = in_text.replace(
'''    add(outlook); add(fullFcst); add(fullBudg); add(budgVar);

    card.appendChild(grid);''',
'''    add(outlook); add(fullFcst); add(fullBudg); add(budgVar); add(day2);

    card.appendChild(grid);'''
)

# 4. renderCrushingGradeForm save payload
in_text = in_text.replace(
'''                full_forecast: parseFloat(fullFcst.input.value),
                full_budget: parseFloat(fullBudg.input.value),
                var3: budgVar.input.value
            }''',
'''                full_forecast: parseFloat(fullFcst.input.value),
                full_budget: parseFloat(fullBudg.input.value),
                var3: budgVar.input.value,
                day2: parseFloat(day2.input.value)
            }'''
)

# 5. renderCrushingGradeForm clear values
in_text = in_text.replace(
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            date.input.value = '';''',
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            day2.input.value = '';
            date.input.value = '';'''
)

# 6. renderCrushingOreForm grid
in_text = in_text.replace(
'''    add(outlook); add(fullFcst); add(fullBudg);
    add(budgVar);

    card.appendChild(grid);''',
'''    add(outlook); add(fullFcst); add(fullBudg);
    add(budgVar); add(day2);

    card.appendChild(grid);'''
)

# 7. renderCrushingOreForm save payload
in_text = in_text.replace(
'''                    full_budget: fullBudg.input.value,
                    var1: dVar.input.value,
                    var2: mVar.input.value,
                    var3: budgVar.input.value
                }''',
'''                    full_budget: fullBudg.input.value,
                    var1: dVar.input.value,
                    var2: mVar.input.value,
                    var3: budgVar.input.value,
                    day2: day2.input.value
                }'''
)

# 8. renderCrushingOreForm clear values
in_text = in_text.replace(
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            date.input.value = '';

        } catch (e) {''',
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            day2.input.value = '';
            date.input.value = '';

        } catch (e) {'''
)

# 9. Ore Crushed Headers
in_text = in_text.replace(
'''                <th style="padding: 12px; text-align: left;">F.Budg</th>
                <th style="padding: 12px; text-align: left;">Var%</th>
                <th style="padding: 12px; text-align: left;">Action</th>
            `;

            if (filteredRecords.length === 0) {
                tbody.innerHTML = `<tr><td colspan="12" style="padding: 12px; text-align: center;">No records found for ${STATE.currentMetric}</td></tr>`;''',
'''                <th style="padding: 12px; text-align: left;">F.Budg</th>
                <th style="padding: 12px; text-align: left;">Var%</th>
                <th style="padding: 12px; text-align: left;">Day-2</th>
                <th style="padding: 12px; text-align: left;">Action</th>
            `;

            if (filteredRecords.length === 0) {
                tbody.innerHTML = `<tr><td colspan="13" style="padding: 12px; text-align: center;">No records found for ${STATE.currentMetric}</td></tr>`;'''
)

# 10. Grade Ore Crushed Headers
in_text = in_text.replace(
'''                <th style="padding: 12px; text-align: left;">F.Budg</th>
                <th style="padding: 12px; text-align: left;">Var%</th>
                <th style="padding: 12px; text-align: left;">Action</th>
            `;

            if (filteredRecords.length === 0) {
                tbody.innerHTML = `<tr><td colspan="13" style="padding: 12px; text-align: center;">No records found for ${STATE.currentMetric}</td></tr>`;''',
'''                <th style="padding: 12px; text-align: left;">F.Budg</th>
                <th style="padding: 12px; text-align: left;">Var%</th>
                <th style="padding: 12px; text-align: left;">Day-2</th>
                <th style="padding: 12px; text-align: left;">Action</th>
            `;

            if (filteredRecords.length === 0) {
                tbody.innerHTML = `<tr><td colspan="14" style="padding: 12px; text-align: center;">No records found for ${STATE.currentMetric}</td></tr>`;'''
)

# 11. Tables Data Cells 
# Both Ore Crushed and Grade have identically structured var3 and action column html:
in_text = in_text.replace(
'''                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>''',
'''                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">${DOM.formatNumber(r.data.day2)}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(in_text)

print("Patch applied successfully")
