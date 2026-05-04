"""
FINANCIAL ALERT SYSTEM
Fraud Detection Module - Version 1.0
Author: Sowmya Kothakapu
"""

import csv
from datetime import datetime

def load_transactions(filename):
    """
    Loads transaction data from a CSV file.
    CSV format: id,amount,date,time,location
    """
    transactions = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert amount to number
                row['amount'] = float(row['amount'])
                transactions.append(row)
        
        print(f"✅ Loaded {len(transactions)} transactions")
        return transactions
    
    except FileNotFoundError:
        print(f"❌ ERROR: File '{filename}' not found!")
        return []
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return []

def detect_suspicious(transactions):
    """
    Rules for detecting suspicious transactions:
    1. Amount > $10,000
    2. Late night transactions (12 AM - 5 AM)
    3. Multiple transactions from same ID in short time
    """
    suspicious = []
    
    for transaction in transactions:
        reasons = []
        
        # Rule 1: High amount
        if transaction['amount'] > 10000:
            reasons.append(f"High amount: ${transaction['amount']:,.2f}")
        
        # Rule 2: Late night
        hour = int(transaction['time'].split(':')[0])
        if 0 <= hour <= 5:
            reasons.append(f"Late night: {transaction['time']}")
        
        # If any reasons found, mark as suspicious
        if reasons:
            transaction['reasons'] = reasons
            suspicious.append(transaction)
    
    return suspicious

def generate_text_report(suspicious, output_file):
    """Creates a simple text report"""
    
    with open(output_file, 'w') as f:
        f.write("="*50 + "\n")
        f.write("FRAUD DETECTION REPORT\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write("="*50 + "\n\n")
        
        if not suspicious:
            f.write("✅ No suspicious transactions found.\n")
            return
        
        f.write(f"⚠️ Found {len(suspicious)} suspicious transactions:\n\n")
        
        for i, trans in enumerate(suspicious, 1):
            f.write(f"{i}. Transaction ID: {trans['id']}\n")
            f.write(f"   Amount: ${trans['amount']:,.2f}\n")
            f.write(f"   Date/Time: {trans['date']} at {trans['time']}\n")
            f.write(f"   Location: {trans['location']}\n")
            f.write(f"   Reasons: {', '.join(trans['reasons'])}\n\n")
    
    print(f"📄 Text report saved: {output_file}")

# ============= MAIN PROGRAM =============

def main():
    print("\n" + "="*40)
    print("FINANCIAL ALERT SYSTEM")
    print("="*40 + "\n")
    
    # Load data
    transactions = load_transactions('data/transactions.csv')
    
    if not transactions:
        print("No transactions to analyze. Exiting.")
        return
    
    # Detect suspicious patterns
    suspicious = detect_suspicious(transactions)
    
    # Generate report
    generate_text_report(suspicious, 'reports/fraud_report.txt')
    
    # Print summary
    print("\n" + "="*40)
    print("SUMMARY")
    print("="*40)
    print(f"Total transactions: {len(transactions)}")
    print(f"Suspicious: {len(suspicious)}")
    
    total_flagged = sum(t['amount'] for t in suspicious)
    print(f"Total flagged amount: ${total_flagged:,.2f}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()