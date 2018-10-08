import smartsheet, json

# Returns a dict of all columns: { 'id'(key) : 'title'(value) }
from dev.config import alleyton_test_sheet_id, ss_user


def get_sheet_columns(sheet_dict, column_dict={}):
    for column in sheet_dict['columns']:
        column_name = column['title']
        column_id = column['id']
        column_dict.update({column_name: column_id})
    return column_dict


# Returns the ID of "Site Name" column
def get_sheet_column_id_site_name(sheet_dict):
    for column in sheet_dict['columns']:
        if 'site' and 'name' in column['title'].lower():
            return column['id']


def get_sheet_column_id_wan_ip(sheet_dict):
    for column in sheet_dict['columns']:
        if 'wan' and 'customer'\
                or 'wan' and 'gateway' in column['title'].lower():
            return column['id']  # 2571976230365060


# Returns a list of all Site Name values in a given sheet
def get_sheet_column_values_site_name(sheet_dict, site_list=[]):
    for row in sheet_dict['rows']:
        for row_cell in row['cells']:
            sheet_site_name_id = get_sheet_column_id_site_name(sheet_dict)
            if row_cell['columnId'] == sheet_site_name_id and "displayValue" in row_cell.keys():
                site_list.append(row_cell['displayValue'])
    return site_list

# TODO: generate_row(): Go through columns, get value from user, append to new dict obj to be pushed to ss_client
#
# TODO: push_sheet_row(generate_row())

# TODO: get_value()
'''
getValue( "Site", "Column Name", sheet): 
    columnToFind(displayValue = "Column Name")
    val = parse("Site Name")
    if val[0] and val[1] in column["Site Name"]:
        
'''


# Create a Smartsheet client object, available functions to this obj in API docs
ss_client = smartsheet.Smartsheet(ss_user['access_token'])
# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)


# Retrieve Smartsheet: "TEST - Alleyton Inventory"
alleyton_sheet = ss_client.Sheets.get_sheet(alleyton_test_sheet_id)
alleyton_sheet_dict = alleyton_sheet.to_dict()

#alleyton_columns = get_sheet_columns(alleyton_sheet_dict)
#alleyton_sites = get_sheet_column_values_site_name(alleyton_sheet_dict)
