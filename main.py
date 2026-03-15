from fastapi import FastAPI
import requests
import pandas as pd

app = FastAPI()

@app.get("/analytics/protein-density")
def analyze_protein_data():
    # 1. Network Request
    url = "https://world.openfoodfacts.org/cgi/search.pl?search_terms=chicken&search_simple=1&json=1&page_size=20"
    response = requests.get(url)
    raw_data = response.json()
    
    # 2. Data Extraction
    products = raw_data.get("products", [])
    extracted_data = []
    
    for item in products:
        name = item.get("product_name", "Unknown")
        nutriments = item.get("nutriments", {})
        protein = nutriments.get("proteins_100g", 0)
        calories = nutriments.get("energy-kcal_100g", 0)
        
        if protein > 0 and calories > 0:
            extracted_data.append({
                "product_name": name, 
                "protein_grams": protein, 
                "calories": calories
            })
            
    # 3. Data Analysis in Memory
    df = pd.DataFrame(extracted_data)
    
    df["protein_per_calorie"] = df["protein_grams"] / df["calories"]
    
    analyzed_df = df.sort_values(by="protein_per_calorie", ascending=False)
    
    # 4. Return Output
    return analyzed_df.to_dict(orient="records")