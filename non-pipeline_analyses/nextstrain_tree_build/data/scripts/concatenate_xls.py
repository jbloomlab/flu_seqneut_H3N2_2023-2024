'''
concatenate_xls.py

Identifies all XLS formatted files in target directory
and returns concatenated XLS.
See usage for specifying input and output. 

'''

import os
import pandas as pd
import xlwt

def concatenate_xls_files(target_dir, output_file):
    all_data = []
    
    for filename in os.listdir(target_dir):
        if filename.endswith(".xls"):
            file_path = os.path.join(target_dir, filename)
            print(f'Found {file_path}, reading...')
            df = pd.read_excel(file_path, engine='xlrd')
            all_data.append(df)
    
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Create a new workbook and write the combined DataFrame to it using xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet1')

    # Write the column headers (row 0 in Excel)
    for col_num, column in enumerate(combined_df.columns):
        sheet.write(0, col_num, column)
    
    # Write the data rows (starting from row 1 in Excel)
    for row_num, row in enumerate(combined_df.values):
        for col_num, value in enumerate(row):
            sheet.write(row_num + 1, col_num, value)

    # Save the workbook as .xls
    workbook.save(output_file)


# Usage
target_dir = './download'
output_file = './concatenated_files/metadata.xls'
os.makedirs('./concatenated_files', exist_ok=True)
concatenate_xls_files(target_dir, output_file)
print('Done.')