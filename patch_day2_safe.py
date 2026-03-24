import sys
import re

file_path = r"c:\Users\nnyame\Desktop\Adamus KPI\frontend\js\app.js"
with open(file_path, 'r', encoding='utf-8') as f:
    in_text = f.read()

in_text = in_text.replace('\r\n', '\n')

def patch_block(text, start_marker, end_marker, old_str, new_str):
    start_idx = text.find(start_marker)
    if start_idx == -1: return text
    end_idx = text.find(end_marker, start_idx)
    if end_idx == -1: return text
    
    block = text[start_idx:end_idx]
    patched_block = block.replace(old_str, new_str)
    return text[:start_idx] + patched_block + text[end_idx:]

# 1. renderCrushingGradeForm
in_text = patch_block(in_text, "function renderCrushingGradeForm(", "function renderCrushingOreForm(",
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);''',
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);

    const day2 = DOM.createInputGroup("Day-2", `input-${dept}-day2`, "number");'''
)

in_text = patch_block(in_text, "function renderCrushingGradeForm(", "function renderCrushingOreForm(",
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }
        } catch (e) {''',
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }
            
            if (d.getDate() === 1) {
                day2.input.value = 0;
            } else {
                const prevDate = new Date(d);
                prevDate.setDate(d.getDate() - 1);
                const pY = prevDate.getFullYear();
                const pM = String(prevDate.getMonth() + 1).padStart(2, '0');
                const pD = String(prevDate.getDate()).padStart(2, '0');
                const prevDateStr = `${pY}-${pM}-${pD}`;
                const prevRecord = records.find(r => r.metric_name === metricName && r.subtype !== 'fixed_input' && r.date === prevDateStr);
                if (prevRecord && prevRecord.data) {
                    day2.input.value = prevRecord.data.daily_actual || 0;
                } else {
                    day2.input.value = 0;
                }
            }
        } catch (e) {'''
)

in_text = patch_block(in_text, "function renderCrushingGradeForm(", "function renderCrushingOreForm(",
'''    add(outlook); add(fullFcst); add(fullBudg); add(budgVar);

    card.appendChild(grid);''',
'''    add(outlook); add(fullFcst); add(fullBudg); add(budgVar); add(day2);

    card.appendChild(grid);'''
)

in_text = patch_block(in_text, "function renderCrushingGradeForm(", "function renderCrushingOreForm(",
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

in_text = patch_block(in_text, "function renderCrushingGradeForm(", "function renderCrushingOreForm(",
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            date.input.value = '';''',
'''            fullBudg.input.value = '';
            budgVar.input.value = '';
            day2.input.value = '';
            date.input.value = '';'''
)

# 2. renderCrushingOreForm
in_text = patch_block(in_text, "function renderCrushingOreForm(", "function renderMillingGoldContainedForm(",
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);''',
'''    const budgVar = DOM.createInputGroup("Var %", `input-${dept}-budg-var`, "text");
    budgVar.input.readOnly = true;
    attachVarianceListener(outlook.input, fullFcst.input, budgVar.input);

    const day2 = DOM.createInputGroup("Day-2", `input-${dept}-day2`, "number");'''
)

in_text = patch_block(in_text, "function renderCrushingOreForm(", "function renderMillingGoldContainedForm(",
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }

            // MTD Calculation''',
'''                fullFcst.input.dispatchEvent(new Event('input', { bubbles: true }));
            }

            if (d.getDate() === 1) {
                day2.input.value = 0;
            } else {
                const prevDate = new Date(d);
                prevDate.setDate(d.getDate() - 1);
                const pY = prevDate.getFullYear();
                const pM = String(prevDate.getMonth() + 1).padStart(2, '0');
                const pD = String(prevDate.getDate()).padStart(2, '0');
                const prevDateStr = `${pY}-${pM}-${pD}`;
                const prevRecord = records.find(r => r.metric_name === metricName && r.subtype !== 'fixed_input' && r.date === prevDateStr);
                if (prevRecord && prevRecord.data) {
                    day2.input.value = prevRecord.data.daily_actual || 0;
                } else {
                    day2.input.value = 0;
                }
            }

            // MTD Calculation'''
)

in_text = patch_block(in_text, "function renderCrushingOreForm(", "function renderMillingGoldContainedForm(",
'''    add(outlook); add(fullFcst); add(fullBudg);
    add(budgVar);

    card.appendChild(grid);''',
'''    add(outlook); add(fullFcst); add(fullBudg);
    add(budgVar); add(day2);

    card.appendChild(grid);'''
)

in_text = patch_block(in_text, "function renderCrushingOreForm(", "function renderMillingGoldContainedForm(",
'''                    full_budget: fullBudg.input.value,
                    var1: dVar.input.value,
                    var2: mVar.input.value,
                    var3: budgVar.input.value
                }''',
'''                    full_budget: fullBudg.input.value,
                    var1: dVar.input.value,
                    var2: mVar.input.value,
                    var3: budgVar.input.value,
                    day2: parseFloat(day2.input.value)
                }'''
)

in_text = patch_block(in_text, "function renderCrushingOreForm(", "function renderMillingGoldContainedForm(",
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

# 3. Tables
# Ore Crushed Header
in_text = patch_block(in_text, "if (STATE.currentMetric === 'Ore Crushed') {", "if (STATE.currentMetric === 'Grade - Ore Mined') {",
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

# Ore Crushed Data
in_text = patch_block(in_text, "if (STATE.currentMetric === 'Ore Crushed') {", "if (STATE.currentMetric === 'Grade - Ore Mined') {",
'''                    <td style="padding: 12px;">${DOM.formatNumber(r.data.full_budget)}</td>
                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>''',
'''                    <td style="padding: 12px;">${DOM.formatNumber(r.data.full_budget)}</td>
                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">${DOM.formatNumber(r.data.day2)}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>'''
)

# Grade Ore Crushed Header
in_text = patch_block(in_text, "if (STATE.currentMetric === 'Grade - Ore Crushed') {", "if (STATE.currentMetric === 'Total Material Moved') {",
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

# Grade Ore Crushed Data
in_text = patch_block(in_text, "if (STATE.currentMetric === 'Grade - Ore Crushed') {", "if (STATE.currentMetric === 'Total Material Moved') {",
'''                    <td style="padding: 12px;">${DOM.formatNumber(r.data.full_budget)}</td>
                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>''',
'''                    <td style="padding: 12px;">${DOM.formatNumber(r.data.full_budget)}</td>
                    <td style="padding: 12px;">${r.data.var3 || '-'}</td>
                    <td style="padding: 12px;">${DOM.formatNumber(r.data.day2)}</td>
                    <td style="padding: 12px;">
                        <button onclick="editRecord(${r.id})" style="margin-right:8px; padding:2px 6px; cursor:pointer;" title="Edit">✏️</button>'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(in_text)

print("Safe patch applied")
