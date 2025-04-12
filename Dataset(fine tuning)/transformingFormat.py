import csv
import json


input_csv = 'data.csv'
output_jsonl = 'clat_dataset.jsonl'


with open(input_csv, 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    
    
    with open(output_jsonl, 'w', encoding='utf-8') as jsonl_file:
        for row in reader:
            
            query = row['Query'].strip()
            answer = row['Answer'].strip()
            
            
            json_object = {
                "text": f"<s>[INST] {query} [/INST] {answer} </s>"
            }
            
            
            jsonl_file.write(json.dumps(json_object, ensure_ascii=False) + '\n')
