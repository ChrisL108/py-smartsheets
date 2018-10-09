import smartsheet
from dev.config import alleyton_test_sheet_id, ss_user


# Returns a dict of all columns: { 'id'(key) : 'title'(value) }
def get_sheet_columns(sheet_dict, column_dict={}):
    for column in sheet_dict['columns']:
        column_name = column['title']
        column_id = column['id']
        column_dict.update({column_name: column_id})
    return column_dict


# Takes a string input and sheet dictionary object and returns the name and ID of the column
#   that matches the string input
def get_column_id(usr_input, sheet_dict):
    usr_input.split(' ')
    stripped_input = usr_input.strip(" ")
    matching_columns = []
    sheet_columns = sheet_dict['columns']
    for column in sheet_columns:
        if stripped_input in column['title']:
            matching_columns.append([column['title'], column['id']])
    return matching_columns


# Returns the ID of "Site Name" column
def get_sheet_column_id_site_name(sheet_dict):
    for column in sheet_dict['columns']:
        title = column['title'].lower()
        if 'site' in title and 'name' in title:
            return column['id']


# Returns the ID of "Customer WAN IP" column
def get_sheet_column_id_wan_ip(sheet_dict):
    for column in sheet_dict['columns']:
        title = column['title'].lower()
        print(title)
        if 'wan' in title and 'customer' in title \
                or 'wan' in title and 'ip' in title:
            return column['id']  # 2571976230365060 / 7075575857735556


# Returns a list of all Site Name values in a given sheet
def get_sheet_site_names(sheet_dict, site_list=[]):
    for row in sheet_dict['rows']:
        for row_cell in row['cells']:
            sheet_site_name_id = get_sheet_column_id_site_name(sheet_dict)
            if row_cell['columnId'] == sheet_site_name_id and "displayValue" in row_cell.keys():
                site_list.append(row_cell['displayValue'])
    return site_list


# TODO: generate_row(): Go through columns, get value from user, append to new dict obj to be pushed to ss_client
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

# alleyton_columns = get_sheet_columns(alleyton_sheet_dict)
# alleyton_sites = get_sheet_site_names(alleyton_sheet_dict)



