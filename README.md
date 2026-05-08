# 💰 Financial Alert System - Fraud Detection

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)]()

> A production-ready fraud detection system that analyzes financial transactions, generates HTML reports with charts, and sends email alerts.

## Features

| Feature | Description |
|---------|-------------|
| **CSV Data Loading** | Reads transaction data from CSV files |
| **Fraud Detection Rules** | Flags high amounts (>$10,000) and late-night transactions |
| **HTML Reports** | Beautiful, responsive HTML reports with Jinja2 templating |
| **Data Visualization** | Bar charts showing amount distribution and hourly patterns |
| **Email Alerts** | Automated email notifications for suspicious activity |
| **Configuration File** | Easy customization without editing code |

## Sample Output

### HTML Report with Charts
![Fraud Detection Report](reports/fraud_charts.png)

### Terminal Output