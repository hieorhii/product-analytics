import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(7)

num_users = 1000
wallets = [f"0x{pd.util.hash_pandas_object(pd.Series([i]))[0]:x}" for i in range(num_users)]

ab_groups = np.random.choice(['A', 'B'], size=num_users, p=[0.8, 0.2])
wallet_ab_map = dict(zip(wallets, ab_groups))

data = []
start_date = datetime(2023, 1, 1)

for _ in range(10000):
    wallet = np.random.choice(wallets)
    group = wallet_ab_map[wallet]
    
    base_amount = np.random.exponential(scale=500)
    amount_usd = base_amount * 1.15 if group == 'B' else base_amount
    
    tx_date = start_date + timedelta(days=np.random.randint(0, 180))
    
    data.append({
        'wallet_address': wallet,
        'tx_date': tx_date.strftime('%Y-%m-%d %H:%M:%S'),
        'amount_usd': round(amount_usd, 2),
        'fee_usd': round(amount_usd * 0.01, 2),
        'ab_group': group
    })

df = pd.DataFrame(data)
df = df.sort_values('tx_date').reset_index(drop=True)
df.to_csv('crypto_txs.csv', index=False)
print("Файл crypto_txs.csv успешно сгенерирован")