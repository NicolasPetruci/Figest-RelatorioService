import io
import pandas as pd
import plotly.express as px

def generate_expenses_chart(df: pd.DataFrame) -> io.BytesIO:
    expenses = df[df['type'] == 'expense']
    category_totals = expenses.groupby('category')['amount'].sum().reset_index()
    
    fig = px.pie(category_totals, values='amount', names='category', title='Expenses by Category')
    
    # Needs kaleido installed for static image export
    img_bytes = fig.to_image(format="png")
    
    buffer = io.BytesIO(img_bytes)
    return buffer
