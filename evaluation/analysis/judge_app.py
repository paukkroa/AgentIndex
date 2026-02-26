"""Interactive Human-in-the-loop Judging App for Evaluation Results."""

import json
import os
from pathlib import Path
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Agentic Index Judge")

RESULTS_PATH = Path("evaluation/results/results.json")
QUESTIONS_PATH = Path("evaluation/dataset/questions.json")

class Rating(BaseModel):
    question_id: str
    system: str
    trial: int
    correctness: float
    completeness: float
    relevance: float
    notes: str = ""

def load_data():
    if not RESULTS_PATH.exists():
        return {"records": []}
    return json.loads(RESULTS_PATH.read_text())

def save_data(data):
    RESULTS_PATH.write_text(json.dumps(data, indent=2))

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Human Judge - Agentic Index</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { padding: 20px; background: #f4f7f6; }
        .comparison-row { display: flex; gap: 20px; margin-bottom: 40px; }
        .system-col { flex: 1; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .gold-box { background: #e7f3ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; border-left: 5px solid #0d6efd; }
        .answer-text { white-space: pre-wrap; background: #fafafa; padding: 10px; border: 1px solid #eee; margin-bottom: 10px; min-height: 150px;}
        .rating-form { margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee; }
        .save-btn { width: 100%; }
        .nav-sidebar { position: sticky; top: 20px; max-height: 90vh; overflow-y: auto; }
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-2 nav-sidebar">
                <h4>Questions</h4>
                <div class="list-group" id="question-list"></div>
            </div>
            <div class="col-md-10">
                <div id="active-question">
                    <h2 class="text-muted">Select a question to begin judging</h2>
                </div>
            </div>
        </div>
    </div>

    <script>
        let resultsData = {};
        let questionsData = {};

        function escapeHtml(text) {
            if (!text) return "";
            const map = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            };
            return text.replace(/[&<>"']/g, function(m) { return map[m]; });
        }

        async function init() {
            const res = await fetch('/data');
            const data = await res.json();
            resultsData = data.results;
            questionsData = data.questions;
            renderList();
        }

        function renderList() {
            const list = document.getElementById('question-list');
            const qIds = [...new Set(resultsData.records.map(r => r.question_id))].sort();
            list.innerHTML = qIds.map(id => `
                <button class="list-group-item list-group-item-action" onclick="showQuestion('${id}', 1)">
                    ${id}
                </button>
            `).join('');
        }

        function showQuestion(qid, trial) {
            const container = document.getElementById('active-question');
            const question = questionsData.find(q => q.id === qid);
            const allTrials = [...new Set(resultsData.records.filter(r => r.question_id === qid).map(r => r.trial))].sort();
            const records = resultsData.records.filter(r => r.question_id === qid && r.trial === trial);
            
            let html = `
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h3>${qid}: ${question.question}</h3>
                    <div class="btn-group">
                        <span class="input-group-text">Trial:</span>
                        ${allTrials.map(t => `
                            <button class="btn btn-sm ${t === trial ? 'btn-primary' : 'btn-outline-primary'}" onclick="showQuestion('${qid}', ${t})">${t}</button>
                        `).join('')}
                    </div>
                </div>
                <div class="gold-box"><strong>Gold Answer:</strong><br>${question.gold_answer}</div>
                <div class="comparison-row">
            `;

            records.forEach(r => {
                const traceId = `trace-${qid}-${trial}-${r.system.replace(/\W/g, '')}`;
                const traceContent = r.retrieved_content ? escapeHtml(r.retrieved_content) : 'No execution trace available for this system.';
                
                let toolCountsStr = "";
                if (r.tool_counts) {
                    toolCountsStr = Object.entries(r.tool_counts)
                        .map(([name, count]) => `<span class="badge bg-info text-dark">${name}: ${count}</span>`)
                        .join(" ");
                }

                html += `
                    <div class="system-col">
                        <h5>${r.system} (Trial ${trial})</h5>
                        <div class="mb-2">${toolCountsStr}</div>
                        <div class="answer-text">${r.answer}</div>
                        <div class="small text-muted mb-2">Retrieved: ${r.retrieved_sources.join(', ')}</div>
                        
                        <button class="btn btn-outline-secondary btn-sm mb-3" onclick="toggleTrace('${traceId}')">Toggle Execution Trace</button>
                        <div id="${traceId}" style="display:none; background: #222; color: #0f0; padding: 10px; font-family: monospace; font-size: 0.8rem; border-radius: 4px; max-height: 300px; overflow-y: auto; white-space: pre-wrap;">${traceContent}</div>

                        <div class="rating-form" id="form-${r.system}-${trial}">
                            <label class="form-label">Correctness (0-5)</label>
                            <input type="number" class="form-control mb-2" id="score-${qid}-${r.system}-${trial}-corr" value="${r.human_correctness || 0}" step="0.5" min="0" max="5">
                            
                            <label class="form-label">Completeness (0-5)</label>
                            <input type="number" class="form-control mb-2" id="score-${qid}-${r.system}-${trial}-comp" value="${r.human_completeness || 0}" step="0.5" min="0" max="5">
                            
                            <button class="btn btn-primary btn-sm save-btn" onclick="saveRating('${qid}', '${r.system}', ${trial})">Save Rating</button>
                        </div>
                    </div>
                `;
            });

            html += '</div>';
            container.innerHTML = html;
        }

        function toggleTrace(id) {
            const el = document.getElementById(id);
            el.style.display = el.style.display === 'none' ? 'block' : 'none';
        }

        async function saveRating(qid, system, trial) {
            const correctness = document.getElementById(`score-${qid}-${system}-${trial}-corr`).value;
            const completeness = document.getElementById(`score-${qid}-${system}-${trial}-comp`).value;
            
            const res = await fetch('/rate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    question_id: qid,
                    system: system,
                    trial: trial,
                    correctness: parseFloat(correctness),
                    completeness: parseFloat(completeness),
                    relevance: 0,
                    notes: ""
                })
            });
            
            if (res.ok) {
                alert(`Rating saved for ${qid} ${system} Trial ${trial}!`);
                resultsData = (await (await fetch('/data')).json()).results;
            } else {
                alert('Error saving rating');
            }
        }

        init();
    </script>
</body>
</html>
"""

@app.get("/data")
async def get_data():
    results = load_data()
    if not Path(QUESTIONS_PATH).exists():
        raise HTTPException(status_code=404, detail="Questions file not found")
    questions = json.loads(QUESTIONS_PATH.read_text())
    return {"results": results, "questions": questions}

@app.post("/rate")
async def rate(rating: Rating):
    data = load_data()
    found = False
    for record in data["records"]:
        if (record["question_id"] == rating.question_id and 
            record["system"] == rating.system and 
            record["trial"] == rating.trial):
            
            # Add human scores to the record
            record["human_correctness"] = rating.correctness
            record["human_completeness"] = rating.completeness
            record["human_evaluated"] = True
            found = True
            break
    
    if not found:
        raise HTTPException(status_code=404, detail="Record not found")
    
    save_data(data)
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8500)
