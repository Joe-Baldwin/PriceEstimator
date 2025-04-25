import schedule
import time
from src.data_ingestion.data_ingestion import ingest_all_vendors

def job():
    print("Checking for vendor price book updates...")
    ingest_all_vendors()

schedule.every().month.do(job)

if __name__ == "__main__":
    print("Starting monthly update job...")
    job()  # Run once at start
    while True:
        schedule.run_pending()
        time.sleep(60 * 60)  # Check hourly
