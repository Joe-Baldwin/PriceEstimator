import os
import sys
import json
from src.data_ingestion.drive_api import get_drive_service, download_file

def handle_list_files(folder_id):
    service = get_drive_service()
    results = service.files().list(q=f"'{folder_id}' in parents and trashed = false", fields="files(id, name)").execute()
    return results.get('files', [])

def handle_download_file(file_id, dest_path):
    download_file(file_id, dest_path)
    return {'status': 'success', 'dest_path': dest_path}

def main():
    print("Google Drive MCP server started")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            action = request.get('action')
            if action == 'list_files':
                folder_id = request['folder_id']
                files = handle_list_files(folder_id)
                print(json.dumps({'files': files}))
            elif action == 'download_file':
                file_id = request['file_id']
                dest_path = request['dest_path']
                result = handle_download_file(file_id, dest_path)
                print(json.dumps(result))
            else:
                print(json.dumps({'error': 'Unknown action'}))
        except Exception as e:
            print(json.dumps({'error': str(e)}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
