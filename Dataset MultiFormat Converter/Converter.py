import pandas as pd
import sqlite3

def converter(input_format, output_format):
    input = input_format.split('.')[-1].lower()
    output = output_format.split('.')[-1].lower()

    if input == 'csv':
        data = pd.read_csv(input_format)
    elif input == 'json':
        data = pd.read_json(input_format)
    elif input == 'xlsx':
        data = pd.read_excel(input_format)
    elif input == 'sqlite':
        conn = sqlite3.connect(input_format)
        data = pd.read_sql_query("SELECT * FROM dataset", conn)
        conn.close()
    elif input == 'h5' or input == 'hdf5':
        data = pd.read_hdf(input_format, key='dataset')
    elif input == 'xml':
        data = pd.read_xml(input_format)
    else:
        raise ValueError("Unsupported format.")

    if output == 'csv':
        data.to_csv(output_format, index=False)
    elif output == 'xlsx':
        data.to_excel(output_format, index=False, engine='openpyxl')
    elif output == 'json':
        data.to_json(output_format, orient='records', lines=True)
    elif output == 'sqlite':
        conn = sqlite3.connect(output_format)
        data.to_sql('dataset', conn, if_exists='replace', index=False)
        conn.close()
    elif output == 'h5' or output == 'hdf5':
        data.to_hdf(output_format, key='dataset', mode='w')
    elif output == 'xml':
        data.to_xml(output_format)
    else:
        raise ValueError("Unsupported format.")

    print(f"Dataset successfully converted from {input} to {output} and saved as {output_format}.")



input_format = input("Enter the input file path: ")
output_format = input("Enter the output file path: ")
converter(input_format, output_format)
