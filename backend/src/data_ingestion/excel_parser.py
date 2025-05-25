import pandas as pd

def parse_excel(file_path, columns, header_row=1):
    # header_row: 1-based (Excel-style), default to 1 (first row)
    df = pd.read_excel(file_path, header=header_row - 1)
    print("Excel columns:", df.columns)
    print("First few rows:\n", df.head())
    try:
        df = df.rename(columns={
            columns['code']: 'code',
            columns['description']: 'description',
            columns['msrp_price']: 'msrp_price',
            columns['internal_cost']: 'internal_cost'
        })
    except Exception as e:
        print("Error renaming columns:", e)
        return []
    try:
        items = df[['code', 'description', 'msrp_price', 'internal_cost']].to_dict(orient='records')
    except Exception as e:
        print("Error selecting columns:", e)
        return []
    print(f"Returning {len(items)} items from Excel parser.")
    return items
