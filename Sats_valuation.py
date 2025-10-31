def read_excel_file(file_path):
    import pandas as pd
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

filename = 'sats-asa-q3-2025-analytical-tool (1).xlsx'
df = read_excel_file(filename)
print(df.columns)

