import json
from pathlib import Path

def find_wins(analysis_path: str):
    print(f"\n--- Analyzing {analysis_path} ---")
    with open(analysis_path, 'r') as f:
        data = json.load(f)
    
    records = data['records']
    # Group by question_id
    by_question = {}
    for r in records:
        qid = r['question_id']
        if qid not in by_question:
            by_question[qid] = {}
        
        sys = r['system']
        if sys not in by_question[qid]:
            by_question[qid][sys] = []
        by_question[qid][sys].append(r)
    
    wins = []
    
    for qid, systems in by_question.items():
        # Find RAG system for this question
        rag_sys = next((s for s in systems.keys() if 'RAG' in s), None)
        if not rag_sys:
            continue
            
        # Calculate average RAG scores
        rag_sim = sum(r['semantic_similarity'] for r in systems[rag_sys]) / len(systems[rag_sys])
        rag_key = sum(r['keyword_recall'] for r in systems[rag_sys]) / len(systems[rag_sys])
        
        for sys_name, records in systems.items():
            if 'Agentic' not in sys_name:
                continue
            
            avg_sim = sum(r['semantic_similarity'] for r in records) / len(records)
            avg_key = sum(r['keyword_recall'] for r in records) / len(records)
            
            if avg_sim > rag_sim or avg_key > rag_key:
                wins.append({
                    'qid': qid,
                    'agentic_sys': sys_name,
                    'rag_sys': rag_sys,
                    'agentic_sim': avg_sim,
                    'rag_sim': rag_sim,
                    'agentic_key': avg_key,
                    'rag_key': rag_key
                })
                
    if not wins:
        print("No cases found where Agentic performed better than RAG.")
    else:
        print(f"Found {len(wins)} cases where Agentic beat RAG.")
        for w in wins[:15]: # Show top 15
            print(f"Q: {w['qid']} | {w['agentic_sys']} vs {w['rag_sys']}")
            print(f"  Sim: {w['agentic_sim']:.3f} vs {w['rag_sim']:.3f} | Key: {w['agentic_key']:.3f} vs {w['rag_key']:.3f}")

if __name__ == "__main__":
    find_wins('evaluation/results/accuracy_analysis_normal.json')
    find_wins('evaluation/results/accuracy_analysis_all.json')
