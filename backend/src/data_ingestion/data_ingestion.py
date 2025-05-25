import os
from src.data_ingestion.drive_api import get_drive_service, download_file
from src.data_ingestion.excel_parser import parse_excel
from src.data_ingestion.pdf_parser import parse_pdf
from src.data_ingestion.sqlite_storage import upsert_item
import json
from datetime import datetime

def ingest_vendor_data(vendor_config):
    service = get_drive_service()
    folder_id = vendor_config['folder_id']
    file_name = vendor_config['file_name']
    query = f"'{folder_id}' in parents and name = '{file_name}' and trashed = false"
    results = service.files().list(q=query, spaces='drive', fields="files(id, name)").execute()
    files = results.get('files', [])
    if not files:
        print(f"No file found for vendor {vendor_config['id']} ({file_name})")
        return
    file_id = files[0]['id']
    local_path = f"/tmp/{vendor_config['id']}_{file_name}"
    download_file(file_id, local_path)
    if vendor_config['file_format'] == 'excel':
        # Support for header row (1-based, default 1)
        header_row = vendor_config.get('header row') or vendor_config.get('header_row') or 1
        items = parse_excel(local_path, vendor_config['columns'], header_row=header_row)
    elif vendor_config['file_format'] == 'pdf':
        items = parse_pdf(local_path, vendor_config['pdf_rules'])
    else:
        print(f"Unknown file format for vendor {vendor_config['id']}")
        return
    for item in items:
        item['vendor_id'] = vendor_config['id']
        item['last_updated'] = datetime.utcnow().isoformat()
        upsert_item(item)
    print(f"Ingested {len(items)} items for vendor {vendor_config['id']}")

def ingest_all_vendors():
    config_path = os.path.join(os.path.dirname(__file__), '../../config/vendor_mapping.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    for vendor in config['vendors']:
        ingest_vendor_data(vendor)
