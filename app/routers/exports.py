from fastapi import APIRouter
from fastapi.responses import Response, StreamingResponse
from app.services.report_service import get_mock_transactions
from app.services.pdf_generator import generate_transactions_pdf
from app.services.chart_generator import generate_expenses_chart

router = APIRouter()

@router.get("/csv")
def export_csv():
    df = get_mock_transactions()
    csv_data = df.to_csv(index=False)
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"}
    )

@router.get("/pdf")
def export_pdf():
    df = get_mock_transactions()
    pdf_buffer = generate_transactions_pdf(df)
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=transactions.pdf"}
    )

@router.get("/chart")
def export_chart():
    df = get_mock_transactions()
    chart_buffer = generate_expenses_chart(df)
    return StreamingResponse(
        chart_buffer,
        media_type="image/png",
        headers={"Content-Disposition": "attachment; filename=chart.png"}
    )
