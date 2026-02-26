#!/bin/bash

# Configuration
PROVIDER="ollama"
MODEL_INDEX="ministral-3" # For indexing
MODEL_EVAL="qwen3:8b"    # For evaluation

echo "----------------------------------------------------------------"
echo "Agentic Index: Full Re-Index and Benchmark Pipeline"
echo "----------------------------------------------------------------"

# 1. Clean Up
echo "[1/4] Cleaning existing indices..."
rm -rf my_knowledge_base my_knowledge_base_scaled

# 2. Build Base Claude Index
echo "[2/4] Initializing and indexing Claude Code docs (NO LIMIT)..."
uv run agentic-index init my_knowledge_base
uv run agentic-index add https://code.claude.com/docs/en/ my_knowledge_base \
  --provider "$PROVIDER" --model "$MODEL_INDEX"

# 3. Build Scaled Index (Claude + Distractors)
echo "[3/4] Building scaled index with distractors..."
cp -r my_knowledge_base my_knowledge_base_scaled

echo "      Adding Python Standard Library docs (NO LIMIT)..."
uv run agentic-index add https://docs.python.org/3/library/ my_knowledge_base_scaled \
  --provider "$PROVIDER" --model "$MODEL_INDEX"

echo "      Adding OpenAI Code Generation docs (NO LIMIT)..."
uv run agentic-index add https://developers.openai.com/codex/ my_knowledge_base_scaled \
  --provider "$PROVIDER" --model "$MODEL_INDEX"

echo "      Adding Purina Dog Breeds (NO LIMIT)..."
uv run agentic-index add https://www.purina.com/dogs/dog-breeds my_knowledge_base_scaled \
  --provider "$PROVIDER" --model "$MODEL_INDEX"

# 4. Run Evaluation
echo "[4/4] Starting Evaluation at $(date)..."
uv run python -m evaluation.runners.run_evaluation \
  --provider "$PROVIDER" \
  --model "$MODEL_EVAL" \
  --scale-test \
  --no-judge

echo "----------------------------------------------------------------"
echo "Pipeline complete! Results saved to evaluation/results/results.json"
echo "----------------------------------------------------------------"
