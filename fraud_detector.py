"""
FINANCIAL ALERT SYSTEM - DAY 2
Fraud Detection with HTML Reports
Author: Sowmya Kothakapu
"""

import csv
import os
from datetime import datetime

# Try to import jinja2 for HTML reports
try:
    from jinja2 import Environment, FileSystemLoader
    JINJA_AVAILABLE = True
    print("✅ Jinja2 loaded - HTML reports enabled")
except ImportError:
    JINJA_AVAILABLE = False
    print("⚠️ Jinja2 not installed. Run: pip install jinja2")

# ============================================
# CONFIGURATION
# ============================================

# File paths
DATA_FILE = "data/transactions.csv"
REPORTS_FOLDER = "reports/"
TEXT_REPORT_NAME = "fraud_report.txt"
HTML_REPORT_NAME = "fraud_report.html"

# Fraud detection rules
AMOUNT_THRESHOLD = 10000
LATE_NIGHT_START = 0
LATE_NIGHT_END = 5

# HTML report setting
GENERATE_HTML = True

# ============================================
# DATA LOADING
# ============================================

def load_transactions(filename):
    """Loads transaction data from a CSV file"""
    transactions = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
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

# ============================================
# FRAUD DETECTION
# ============================================

def detect_suspicious(transactions):
    """Detects suspicious transactions"""
    suspicious = []
    
    for transaction in transactions:
        reasons = []
        
        # Rule 1: High amount
        if transaction['amount'] > AMOUNT_THRESHOLD:
            reasons.append(f"High amount: ${transaction['amount']:,.2f}")
        
        # Rule 2: Late night
        try:
            hour = int(transaction['time'].split(':')[0])
            if LATE_NIGHT_START <= hour <= LATE_NIGHT_END:
                reasons.append(f"Late night: {transaction['time']}")
        except:
            pass
        
        if reasons:
            transaction['reasons'] = reasons
            suspicious.append(transaction)
    
    return suspicious

# ============================================
# TEXT REPORT GENERATION
# ============================================

def generate_text_report(suspicious, total_transactions, output_file):
    """Creates a plain text report"""
    
    # Ensure reports folder exists
    os.makedirs(REPORTS_FOLDER, exist_ok=True)
    
    output_path = os.path.join(REPORTS_FOLDER, output_file)
    
    with open(output_path, 'w') as f:
        f.write("="*50 + "\n")
        f.write("FRAUD DETECTION REPORT\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write("="*50 + "\n\n")
        
        f.write(f"Total Transactions: {total_transactions}\n")
        f.write(f"Suspicious: {len(suspicious)}\n")
        
        total_flagged = sum(t['amount'] for t in suspicious)
        f.write(f"Total Flagged Amount: ${total_flagged:,.2f}\n\n")
        
        if not suspicious:
            f.write("✅ No suspicious transactions found.\n")
            return output_path
        
        f.write("⚠️ SUSPICIOUS TRANSACTIONS:\n\n")
        
        for i, trans in enumerate(suspicious, 1):
            f.write(f"{i}. Transaction ID: {trans['id']}\n")
            f.write(f"   Amount: ${trans['amount']:,.2f}\n")
            f.write(f"   Date/Time: {trans['date']} at {trans['time']}\n")
            f.write(f"   Location: {trans['location']}\n")
            f.write(f"   Reasons: {', '.join(trans['reasons'])}\n\n")
    
    print(f"📄 Text report saved: {output_path}")
    return output_path

# ============================================
# HTML REPORT GENERATION
# ============================================

def generate_html_report(suspicious, total_transactions, output_file):
    """Creates a beautiful HTML report"""
    
    if not JINJA_AVAILABLE:
        print("⚠️ HTML report skipped - install jinja2 first")
        return None
    
    # Ensure reports folder exists
    os.makedirs(REPORTS_FOLDER, exist_ok=True)
    
    output_path = os.path.join(REPORTS_FOLDER, output_file)
    
    # Calculate totals
    total_flagged = sum(t['amount'] for t in suspicious)
    
    # Prepare data for template
    template_data = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'total_transactions': total_transactions,
        'suspicious_count': len(suspicious),
        'total_flagged_amount': f"{total_flagged:,.2f}",
        'suspicious': suspicious
    }
    
    # Load and render template
    try:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')
        html_content = template.render(**template_data)
        
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        print(f"🌐 HTML report saved: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"❌ Error generating HTML report: {e}")
        return None

# ============================================
# MAIN PROGRAM
# ============================================

def main():
    print("\n" + "="*50)
    print("💰 FINANCIAL ALERT SYSTEM - DAY 2")
    print("Fraud Detection with HTML Reports")
    print("="*50 + "\n")
    
    # Load data
    transactions = load_transactions(DATA_FILE)
    
    if not transactions:
        print("No transactions to analyze. Exiting.")
        return
    
    # Detect suspicious patterns
    suspicious = detect_suspicious(transactions)
    
    # Generate text report (always)
    generate_text_report(suspicious, len(transactions), TEXT_REPORT_NAME)
    
    # Generate HTML report (if enabled)
    if GENERATE_HTML:
        generate_html_report(suspicious, len(transactions), HTML_REPORT_NAME)
    
    # Print summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Total transactions: {len(transactions)}")
    print(f"Suspicious: {len(suspicious)}")
    
    total_flagged = sum(t['amount'] for t in suspicious)
    print(f"Total flagged amount: ${total_flagged:,.2f}")
    print("="*50 + "\n")
    
    print("🎉 Day 2 complete!")
    print("   📄 Text report saved")
    if JINJA_AVAILABLE and GENERATE_HTML:
        print("   🌐 HTML report saved - open it in your browser!")

if __name__ == "__main__":
    main()