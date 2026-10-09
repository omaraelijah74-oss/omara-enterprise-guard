# REAL $4000/mo Client - $50k spend
print("--- $4000/MO CLIENT AUDIT ---")
usage=[
  ["GPT-4 Support Bot - 500k chats/day", 50000000, 15000],
  ["GPT-4 Docs Summarizer", 40000000, 12000],
  ["Claude Code Assistant", 30000000, 9000],
  ["Embeddings + Vector Search", 20000000, 8000],
  ["Fine-tuned Models", 0, 6000],
]

total_old = sum(c for _,_,c in usage)
save_total=0
for task, tokens, cost in usage:
  new_cost = cost * 0.3
  save = cost - new_cost
  save_total+=save
  print(f"{task[:25]}: ${cost} -> ${int(new_cost)} SAVE ${int(save)}")

print(f"\nOLD: ${total_old}/mo = ${total_old*12}/year")
print(f"SAVE: ${int(save_total)}/mo = ${int(save_total*12)}/year")
print(f"YOU CHARGE: $4000/mo")
print(f"CLIENT PROFIT: ${int(save_total-4000)}/mo = ${int((save_total-4000)*12)}/year!")
print(f"Client ROI: {int(save_total/4000*100)}%")
