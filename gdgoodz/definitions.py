import os

# Project's root directory path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# FIle export paths
XLSX_DIR    = os.path.join(ROOT_DIR, 'exports/xlsx')
CSV_DIR     = os.path.join(ROOT_DIR, 'exports/csv')
JSON_DIR    = os.path.join(ROOT_DIR, 'exports/json')