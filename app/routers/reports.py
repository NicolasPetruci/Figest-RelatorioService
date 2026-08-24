from fastapi import APIRouter

router = APIRouter()

@router.get("/monthly")
def get_monthly_report(month: int, year: int):
    return {"message": "Monthly report", "month": month, "year": year}

@router.get("/annual")
def get_annual_report(year: int):
    return {"message": "Annual report", "year": year}

@router.get("/category-breakdown")
def get_category_breakdown(period: str):
    return {"message": "Category breakdown", "period": period}

@router.get("/trend")
def get_trend_report(months: int = 6):
    return {"message": "Trend report", "months": months}
