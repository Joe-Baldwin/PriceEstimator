from fastapi import APIRouter, HTTPException, BackgroundTasks, Response
from fastapi.responses import FileResponse
from src.data_ingestion.sqlite_storage import get_items_by_vendor
from .email_utils import send_estimate_email
from .export_utils import export_items_to_excel
import tempfile
import os

router = APIRouter()

@router.get("/vendors/{vendor_id}/items")
def get_items(vendor_id: str):
    items = get_items_by_vendor(vendor_id)
    if items is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return items

@router.post("/email_estimate")
def email_estimate(payload: dict, background_tasks: BackgroundTasks):
    # payload: { to_email, subject, items: [{description, msrp_price}], total }
    to_email = payload.get("to_email")
    subject = payload.get("subject", "Your Estimate")
    items = payload.get("items", [])
    total = payload.get("total", 0)
    html_rows = "".join([f"<tr><td>{item['description']}</td><td>${item['msrp_price']:.2f}</td></tr>" for item in items])
    html_content = f"""
    <h3>Estimate</h3>
    <table border='1'><tr><th>Description</th><th>MSRP Price</th></tr>{html_rows}</table>
    <p><b>Total: ${total:.2f}</b></p>
    """
    background_tasks.add_task(send_estimate_email, to_email, subject, html_content)
    return {"message": "Email sent (queued)"}

@router.get("/export/vendors")
def export_vendors():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        export_items_to_excel(tmp.name)
        tmp_path = tmp.name
    filename = "ServiceTitan_Vendor_Items.xlsx"
    headers = {"Content-Disposition": f"attachment; filename={filename}"}
    return FileResponse(tmp_path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers=headers)
