import json, os

source_file = "../invoices.json"
output_folder = "../API/invoices"
os.makedirs(output_folder, exist_ok=True)

with open(source_file, "r") as f:
    invoices = json.load(f)

for invoice in invoices:
    invoice_id = str(invoice["id"]) + ".json"  # add .json extension
    with open(os.path.join(output_folder, invoice_id), "w") as out:
        json.dump(invoice, out, indent=2)

print(f"Created {len(invoices)} files with .json extension")
