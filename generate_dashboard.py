import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def create_dashboard():
    # Set aesthetics
    sns.set_theme(style="whitegrid")
    
    # Load data
    with open('evaluation/results/accuracy_analysis_normal.json', 'r') as f:
        normal_recs = json.load(f)['records']
    with open('evaluation/results/accuracy_analysis_all.json', 'r') as f:
        scaled_recs = json.load(f)['records']
        
    df_norm = pd.DataFrame(normal_recs)
    df_norm['dataset'] = 'Normal'
    
    df_scaled = pd.DataFrame(scaled_recs)
    df_scaled['dataset'] = 'Scaled'
    
    # Combine and simplify system names for cleaner plotting
    df = pd.concat([df_norm, df_scaled])
    
    def simplify_sys(name):
        if 'Hybrid-RAG' in name or 'RAG(' in name:
            return 'RAG'
        if 'Agentic' in name:
            if 'navigational' in name: return 'Agentic (Nav)'
            if 'simplified' in name: return 'Agentic (Simp)'
            if 'explicit' in name: return 'Agentic (Expl)'
            return 'Agentic'
        return name
    
    df['system_type'] = df['system'].apply(simplify_sys)
    
    # Create the dashboard layout (2x2 grid)
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Agentic Index vs RAG: Performance Dashboard', fontsize=22, fontweight='bold')
    
    # 1. Semantic Similarity by System and Dataset
    sns.barplot(ax=axes[0,0], data=df, x='system_type', y='semantic_similarity', hue='dataset')
    axes[0,0].set_title('Overall Semantic Similarity (Accuracy)', fontsize=16)
    axes[0,0].set_ylim(0, 1.0)
    
    # 2. Keyword Recall by Category (Focused on Normal dataset for clarity)
    sns.barplot(ax=axes[0,1], data=df_norm, x='category', y='keyword_recall', hue='system')
    axes[0,1].set_title('Keyword Recall by Category (Normal Dataset)', fontsize=16)
    axes[0,1].set_ylim(0, 1.0)
    
    # 3. Latency vs Accuracy Scatter (Scaled Dataset)
    # Filter for Scaled and the primary comparison systems
    df_scaled_filtered = df[(df['dataset'] == 'Scaled') & (df['system_type'].isin(['RAG', 'Agentic (Nav)']))]
    sns.scatterplot(ax=axes[1,0], data=df_scaled_filtered, x='latency_ms', y='semantic_similarity', 
                    hue='system_type', style='category', s=100)
    axes[1,0].set_title('Latency vs Accuracy (Scaled Dataset)', fontsize=16)
    axes[1,0].set_xlabel('Latency (ms)')
    
    # 4. Accuracy Drop: Normal vs Scaled (Noise Resilience)
    # Group by system_type and dataset
    noise_df = df.groupby(['system_type', 'dataset'])['semantic_similarity'].mean().reset_index()
    sns.pointplot(ax=axes[1,1], data=noise_df, x='dataset', y='semantic_similarity', hue='system_type', markers=["o", "s", "D", "v", "^"])
    axes[1,1].set_title('Noise Resilience: Normal vs Scaled', fontsize=16)
    axes[1,1].set_ylabel('Mean Semantic Similarity')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Save the dashboard
    output_path = Path('evaluation/report/performance_dashboard.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    print(f"Dashboard saved to {output_path}")

if __name__ == "__main__":
    create_dashboard()
