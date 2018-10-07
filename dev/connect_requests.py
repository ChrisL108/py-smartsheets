import json, requests, pandas as pd
from config import ss_user


solis_test_sheet_id = 3073042256553860

ss_url = "https://api.smartsheet.com/2.0/sheets"
ss_auth = f"Bearer {ss_user["access_token"]}"
ss_cont_type = "application/json"
