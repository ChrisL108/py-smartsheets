import smartsheet
from config import *
# import pandas as pd, json


# Returns a dict of all columns: { 'id'(key) : 'title'(value) }
def get_column_dict(sheet_dict, column_dict={}):
    for column in sheet_dict['columns']:
        column_name = column['title']
        column_id = column['id']
        column_dict.update({column_name: column_id})
    return column_dict


# Returns the ID of Site Name column
def get_site_name_id(sheet_dict):
    for column in sheet_dict['columns']:
        if 'site' and 'name' in column['title'].lower():
            return column['id']


# Returns a list of all Site Name values in a given sheet
def get_site_name_list(sheet_dict, site_list=[]):
    for row in sheet_dict['rows']:
        for row_cell in row['cells']:
            sheet_site_name_id = get_site_name_id(sheet_dict)
            if row_cell['columnId'] == sheet_site_name_id and "displayValue" in row_cell.keys():
                site_list.append(row_cell['displayValue'])
    return site_list


# Create a Smartsheet client object, available functions to this obj in API docs
ss_client = smartsheet.Smartsheet(ss_user['access_token'])
# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)



# Retrieve Smartsheet: "TEST - Alleyton Inventory"
alleyton_test_sheet = ss_client.Sheets.get_sheet(alleyton_test_sheet_id)
alleyton_sheet_dict = alleyton_test_sheet.to_dict()

# get_column_dict(custom_sheet_dict)
# get_site_name_list(custom_sheet_dict)

'''
    solis_sheet_id = 3073042256553860
    alleyton_sheet_id = 5850406480832388
'''