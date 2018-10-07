import smartsheet
from config import ss_user
# import pandas as pd, json


def get_columns(sheet_dict, column_dict={}):
    for column in sheet_dict['columns']:
        column_name = column['title']
        column_id = column['id']
        column_dict.update({column_name: column_id})
    return column_dict


def get_site_names(sheet_dict, site_list=[]):
    for row in sheet_dict['rows']:
        for row_cell in row['cells']:
            # TODO: find_siteName_column_id() function
            # find_siteName_column_id(sheet_dict)
            if row_cell['columnId'] == 5562647857915780 and "displayValue" in row_cell.keys():
                site_list.append(row_cell['displayValue'])
    return site_list


# Create a Smartsheet client object, available functions to this obj in API docs
ss_client = smartsheet.Smartsheet(ss_user['access_token'])
# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)

solis_test_sheet_id = 3073042256553860
alleyton_test_sheet_id = 5850406480832388
# Retrieve Smartsheet: "TEST - Alleyton Inventory"
current_sheet = ss_client.Sheets.get_sheet(alleyton_test_sheet_id)

# TODO: test dictionary object for function testing
custom_sheet_dict = current_sheet.to_dict()


''' 
MODEL FOR UPDATING SMARTSHEET

updated_sheet = ss_client.Sheets.update_sheet(
    solis_test_sheet_id,       # sheet_id
    ss_client.models.Sheet({
        'name': '--New Name--'
    })
)

'''

