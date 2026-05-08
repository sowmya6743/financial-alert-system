"""
Chart Generator for Fraud Detection System
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

def generate_fraud_charts(transactions, suspicious, output_folder="reports"):
    """Generate charts showing fraud patterns"""
    
    if not transactions:
        print("No transactions to chart")
        return None
    
    # Create DataFrame
    df = pd.DataFrame(transactions)
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Create figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Chart 1: Amount Distribution
    suspicious_ids = [t['id'] for t in suspicious]
    normal_amounts = df[~df['id'].isin(suspicious_ids)]['amount']
    fraud_amounts = df[df['id'].isin(suspicious_ids)]['amount']
    
    ax1.hist([normal_amounts, fraud_amounts], bins=20, 
             label=['Normal', 'Suspicious'], alpha=0.7, 
             color=['green', 'red'])
    ax1.set_xlabel('Transaction Amount ($)')
    ax1.set_ylabel('Number of Transactions')
    ax1.set_title('Transaction Amount Distribution')
    ax1.legend()
    
    # Chart 2: Suspicious by Hour
    suspicious_df = df[df['id'].isin(suspicious_ids)].copy()
    if len(suspicious_df) > 0:
        suspicious_df['hour'] = suspicious_df['time'].apply(lambda x: int(x.split(':')[0]))
        hour_counts = suspicious_df['hour'].value_counts().sort_index()
        
        hours = list(range(24))
        counts = [hour_counts.get(h, 0) for h in hours]
        
        ax2.bar(hours, counts, color='red', alpha=0.7)
        ax2.set_xlabel('Hour of Day')
        ax2.set_ylabel('Suspicious Transactions')
        ax2.set_title('Suspicious Transactions by Hour')
        ax2.set_xticks(range(0, 24, 3))
    else:
        ax2.text(0.5, 0.5, 'No suspicious transactions', 
                 ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title('Suspicious Transactions by Hour')
    
    # Add overall title
    fig.suptitle(f'Fraud Analysis Report - {datetime.now().strftime("%Y-%m-%d")}', 
                 fontsize=14, fontweight='bold')
    
    # Save the chart
    os.makedirs(output_folder, exist_ok=True)
    chart_path = os.path.join(output_folder, 'fraud_charts.png')
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"📊 Charts saved: {chart_path}")
    return chart_path

print("Chart generator module loaded successfully!")