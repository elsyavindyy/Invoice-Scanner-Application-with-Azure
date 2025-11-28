import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

endpoint = "ENTER YOUR ENDPOINT HERE"
key = "ENTER YOUR KEY HERE"
model_id = "ENTER YOU MODEL ID HERE"


client = DocumentIntelligenceClient(endpoint, AzureKeyCredential(key))
def run_scan(image_path):
    lokal_file = image_path
    with open(lokal_file, "rb") as f:
        poller = client.begin_analyze_document(
            model_id=model_id,
            body=f
        )

    result = poller.result()
    doc = result.documents[0]
    fields = doc.fields

    # =====================================
    # DICTIONARY FINAL UNTUK JSON
    # =====================================
    final_json = {}

    for field_name, field_data in fields.items():

        # 1️⃣ LIST (contoh: Item)
        if field_data["type"] == "array":
            array_items = list(field_data.values())[1]

            rows = []
            for row in array_items:
                obj = row["valueObject"]
                row_dict = {}

                for col_name, col_field in obj.items():
                    row_dict[col_name] = (
                        col_field.get("valueString") 
                        or col_field.get("valueNumber") 
                        or col_field.get("valueDate")
                    )

                rows.append(row_dict)

            final_json[field_name] = rows
            continue

        # 2️⃣ OBJECT (contoh: INFO, Total)
        if field_data["type"] == "object":
            obj = field_data["valueObject"]
            obj_dict = {}

            for sub_label, sub_field in obj.items():
                obj_dict[sub_label] = (
                    sub_field.get("valueString") 
                    or sub_field.get("valueNumber") 
                    or sub_field.get("valueDate")
                )

            final_json[field_name] = obj_dict
            continue

        # 3️⃣ FIELD SIMPLE
        final_json[field_name] = (
            field_data.get("valueString") 
            or field_data.get("valueNumber") 
            or field_data.get("valueDate")
        )

    return final_json

# Kalau mau simpan ke file:
# with open("output_invoice.json", "w", encoding="utf-8") as out:
#     json.dump(final_json, out, indent=4, ensure_ascii=False)
