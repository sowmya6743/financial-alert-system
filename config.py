"""
Configuration file for Financial Alert System
Edit this file to customize your fraud detection settings
"""

# ============================================
# EMAIL CONFIGURATION
# ============================================

# Sender email (must be Gmail for this tutorial)
EMAIL_SENDER = "sowmyareddy3476@gmail.com"  # ← CHANGE THIS!

# App Password (NOT your regular Gmail password)
# Get it from: https://myaccount.google.com/apppasswords
EMAIL_PASSWORD = "bsba kqrn gelj zggk"  # ← CHANGE THIS!

# Recipient email (where alerts will be sent)
EMAIL_RECIPIENT = "sowmya.reddie1@gmail.com"  # ← CHANGE THIS!

# Email subject line
EMAIL_SUBJECT = "🚨 FRAUD ALERT: Suspicious Transactions Detected"

# ============================================
# FRAUD DETECTION RULES
# ============================================

# Amount threshold (transactions above this are flagged)
AMOUNT_THRESHOLD = 10000  # $10,000

# Late night hours (0-23)
LATE_NIGHT_START = 0  # 12 AM
LATE_NIGHT_END = 5    # 5 AM

# ============================================
# REPORT CONFIGURATION
# ============================================

# Generate HTML report?
GENERATE_HTML = True

# HTML report filename
HTML_REPORT_NAME = "fraud_report.html"

# Text report filename
TEXT_REPORT_NAME = "fraud_report.txt"

# ============================================
# FILE PATHS
# ============================================

DATA_FILE = "data/transactions.csv"
REPORTS_FOLDER = "reports/"