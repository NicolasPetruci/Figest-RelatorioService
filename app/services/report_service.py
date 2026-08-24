import pandas as pd
from datetime import datetime, timedelta
import random

def get_mock_transactions() -> pd.DataFrame:
    # Generate 50 dummy transactions
    categories = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Salary', 'Rent']
    types = ['income', 'expense']
    
    data = []
    base_date = datetime.now()
    
    for i in range(50):
        t_type = random.choices(types, weights=[0.2, 0.8])[0]
        cat = 'Salary' if t_type == 'income' else random.choice([c for c in categories if c != 'Salary'])
        amount = random.uniform(10, 150) if t_type == 'expense' else random.uniform(1000, 3000)
        
        data.append({
            'date': (base_date - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d'),
            'type': t_type,
            'category': cat,
            'amount': round(amount, 2),
            'description': f"Mock {cat} transaction"
        })
        
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date', ascending=False)
    return df
