# AI Cost Audit Tool - Worth $4000/mo
print("--- AI COST AUDIT ---")
usage=[
  ["GPT-4 summary", 1000000, 30], # 1M tokens $30
  ["GPT-4 classification", 2000000, 60],
]

waste=0
for task, tokens, cost in usage:
  new_cost = cost * 0.1 # Route to mini = 90% saving
  save = cost - new_cost
  waste+=save
  print(f"{task}: ${cost} -> ${new_cost} SAVE ${save}")

print(f"\nTOTAL SAVE: ${waste}/mo = ${waste*12}/year")
print(f"Your fee $4000/mo -> Client profit ${waste-4000}/mo")
