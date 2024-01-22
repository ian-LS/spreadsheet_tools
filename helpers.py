import pandas as pd
from io import BytesIO

def validate_format(file1, file2):
    try:
        df1 = read_dataframe(file1)
        df2 = read_dataframe(file2)

        return df1.columns.tolist() == df2.columns.tolist()
    except pd.errors.EmptyDataError:
        return False

def read_dataframe(file):
    # Read CSV or Excel file based on file extension
    if file.filename.endswith('.csv'):
        return pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        return pd.read_excel(file, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel (xlsx) files are accepted.")


def merge_documents(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    merged_data = pd.concat([df1, df2], ignore_index=True)
    merged_csv = merged_data.to_csv(index=False)

    return merged_csv

def remove_duplicates(file):
    df = pd.read_csv(file)
    cleaned_data = df.drop_duplicates().to_csv(index=False)

    return cleaned_data
