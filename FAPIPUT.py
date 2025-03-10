from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dictionary containing famous foods from each Indian state
indian_state_foods = {
    "Andhra Pradesh": ["Hyderabadi Biryani", "Gongura Pickle", "Pesarattu", "Pootha Rekulu"],
    "Arunachal Pradesh": ["Thukpa", "Momos", "Zan", "Chura Sabzi"],
    "Assam": ["Assam Laksa", "Masor Tenga", "Aloo Pitika", "Pithas"],
    "Bihar": ["Litti Chokha", "Sattu Paratha", "Thekua", "Khaja"],
    "Chhattisgarh": ["Chana Samosa", "Aamat", "Farra", "Bafauri"],
    "Goa": ["Goan Fish Curry", "Bebinca", "Pork Vindaloo", "Sannas"],
    "Gujarat": ["Dhokla", "Thepla", "Undhiyu", "Khandvi"],
    "Haryana": ["Bajra Khichdi", "Besan Masala Roti", "Bajre Ki Roti", "Singri Sabzi"],
    "Himachal Pradesh": ["Dham", "Siddu", "Babru", "Chana Madra"],
    "Jharkhand": ["Dhuska", "Thekua", "Rugra", "Litti Chokha"],
    "Karnataka": ["Bisi Bele Bath", "Mysore Pak", "Neer Dosa", "Ragi Mudde"],
    "Kerala": ["Appam with Stew", "Puttu and Kadala Curry", "Sadya", "Erissery"],
    "Madhya Pradesh": ["Poha Jalebi", "Dal Bafla", "Bhutte Ka Kees", "Chakki Ki Shaak"],
    "Maharashtra": ["Pav Bhaji", "Vada Pav", "Puran Poli", "Misal Pav"],
    "Manipur": ["Eromba", "Kangshoi", "Ngari", "Chak-hao Kheer"],
    "Meghalaya": ["Jadoh", "Dohneiiong", "Pumaloi", "Nakham Bitchi"],
    "Mizoram": ["Bai", "Vawksa Rep", "Sanpiau", "Chhangban"],
    "Nagaland": ["Smoked Pork", "Bamboo Shoot Curry", "Axone", "Zutho"],
    "Odisha": ["Dalma", "Chhena Poda", "Pakhala Bhata", "Rasagola"],
    "Punjab": ["Makki Di Roti & Sarson Da Saag", "Chole Bhature", "Butter Chicken", "Paneer Tikka"],
    "Rajasthan": ["Dal Baati Churma", "Gatte Ki Sabzi", "Ker Sangri", "Laal Maas"],
    "Sikkim": ["Phagshapa", "Momos", "Thukpa", "Sha Phaley"],
    "Tamil Nadu": ["Dosa", "Idli Sambar", "Chettinad Chicken", "Pongal"],
    "Telangana": ["Hyderabadi Biryani", "Sakinalu", "Golgappa", "Pesarattu"],
    "Tripura": ["Mui Borok", "Chuak", "Mosdeng Serma", "Gudok"],
    "Uttar Pradesh": ["Tunday Kababi", "Peda", "Puri Aloo", "Bedai"],
    "Uttarakhand": ["Aloo Ke Gutke", "Chainsoo", "Kafuli", "Jhangora Ki Kheer"],
    "West Bengal": ["Rosogolla", "Shorshe Ilish", "Aloo Posto", "Macher Jhol"]
}

class FoodUpdate(BaseModel):
    new_foods: List[str]

@app.get("/get_updated_state_food/{state}")
async def updated_state_food(state: str):
    if state in  indian_state_foods:
        return {"state": state, "food_items": indian_state_foods[state]}
    else:
        return {"state": state, "food_items": indian_state_foods[state]}

@app.post("/add_state_food/{state}")
async def add_state_food(state: str, food_update: FoodUpdate):
    # Check if the state exists
    if state not in indian_state_foods:
        return {"error": "State not found"}
    
    indian_state_foods[state].extend(food_update.new_foods)
    
    return {"message": f"New food items added for {state}!", "updated_foods": indian_state_foods[state]}

@app.put("/update_state_food/{state}")
async def update_state_food(state: str, food_update: FoodUpdate):

    if state not in indian_state_foods:
        return {"error": "State not found"}

    indian_state_foods[state] = food_update.new_foods
    return {"message": f"Food items for {state} updated successfully!", "updated_foods": indian_state_foods[state]}

@app.delete("/delete_state_food/{state}")
async def deleted_state_food(state: str):
    if state in indian_state_foods:
        del indian_state_foods[state]
        return {"message":f"Food data for {state} has been deleted succesfully"}
    else:
        return {"error":f"State not found"}
    