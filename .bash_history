nano scan.py
cat > scan.py << 'END'
print("--- AWS WASTE SCAN ---")
print("")
servers = [
    ["i-123 - Old Dev Server", 2, 450],
    ["i-456 - Backup from 2024", 0, 820],
    ["i-789 - Production (OK)", 75, 120],
]
total_waste = 0
for name, cpu, cost in servers:
    if cpu < 5:
        print(f"FOUND WASTE: {name}")
        print(f"  CPU: {cpu}% - Cost: ${cost}/month")
        print(f"  ACTION: Can stop safely")
        print("")
        total_waste += cost
    else:
        print(f"OK: {name} - CPU {cpu}% - Keep running")
        print("")
print(f"TOTAL WASTE FOUND: ${total_waste}/month")
print(f"YEARLY: ${total_waste * 12}")
ENDrm scan.py

rm scan.py
python -c "open('scan.py','w').write('print(\"--- AWS WASTE SCAN ---\")\nservers=[[\"i-123 Old Dev\",2,450],[\"i-456 Backup 2024\",0,820],[\"i-789 Prod OK\",75,120]]\ntotal=0\nfor n,c,p in servers:\n if c<5:\n  print(f\"WASTE: {n} CPU {c}% ${p}/mo\")\n  total+=p\n else:\n  print(f\"OK: {n} CPU {c}%\")\nprint(f\"TOTAL WASTE: ${total}/mo YEARLY ${total*12}\")\n')"
python scan.py
rm -f scan.py; cat > /tmp/a.py << 'EE'
print("--- AWS WASTE SCAN ---")
servers=[["i-123 Old Dev",2,450],["i-456 Backup",0,820],["i-789 Prod",75,120]]
total=0
for n,c,p in servers:
 if c<5:
  print("WASTE:",n,"CPU",c,"% $"+str(p)+"/mo")
  total+=p
 else:
  print("OK:",n)
print("TOTAL WASTE: $"+str(total)+"/mo YEARLY $"+str(total*12))
EE

rm -f scan.py
cat > scan.py << 'EE'
print("--- AWS WASTE SCAN ---")
waste=1270
print("WASTE: i-123 Old Dev CPU 2% $450/mo")
print("WASTE: i-456 Backup CPU 0% $820/mo")
print("OK: i-789 Prod CPU 75%")
print("TOTAL WASTE: $1270/mo YEARLY $15240")
EE

python scan.py
/
