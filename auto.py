print("=== Omara's $20K/MO Automation ===\n")

clients = [
  {"name": "Client1 SaaS", "bill": 50000},
  {"name": "Client2 AI Startup", "bill": 30000},
  {"name": "Client3 Fintech", "bill": 40000},
  {"name": "Client4 HealthTech", "bill": 25000},
  {"name": "Client5 EdTech", "bill": 60000},
]

total_earn = 0
total_saved = 0

for c in clients:
    old = c["bill"]
    new = int(old * 0.3)
    save = old - new
    fee = 4000
    total_earn += fee
    total_saved += save
    print(f"{c['name']}")
    print(f"  Bill: ${old} -> ${new}")
    print(f"  Client Save: ${save}/mo | You Earn: ${fee}/mo\n")

print(f"YOU EARN: ${total_earn}/mo = ${total_earn*12}/year")
print(f"CLIENTS SAVE: ${total_saved}/mo")
print("\nOmara + AI = $4000/mo per client - AUTOMATED!")
