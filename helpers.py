import pandas as pd
from io import BytesIO

def validate_format(file1, file2):
    try:
        df1 = read_dataframe(file1)
        df2 = read_dataframe(file2)

        return df1.columns.tolist() == df2.columns.tolist()
    except pd.errors.EmptyDataError:
        return False

def merge_documents(file1, file2):
    df1 = read_dataframe(file1)
    df2 = read_dataframe(file2)

    merged_data = pd.concat([df1, df2], ignore_index=True)
    merged_csv = merged_data.to_csv(index=False)

    return merged_csv

def remove_duplicates(file):
    df = read_dataframe(file)
    cleaned_data = df.drop_duplicates().to_csv(index=False)

    return cleaned_data

def read_dataframe(file, **kwargs):
    # Read CSV or Excel file based on file extension
    if file.filename.endswith('.csv'):
        try:
            return pd.read_csv(file, **kwargs)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()  # Return an empty DataFrame if the file is empty
    elif file.filename.endswith('.xlsx'):
        try:
            return pd.read_excel(file, engine='openpyxl', **kwargs)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()  # Return an empty DataFrame if the file is empty
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel (xlsx) files are accepted.")
