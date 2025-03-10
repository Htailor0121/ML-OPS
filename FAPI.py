from fastapi import FastAPI
from enum import Enum

app = FastAPI()


food_items = {
	
    "Italy": ["Pizza", "Pasta", "Lasagna"],
    "France": ["Baguette", "Croissant", "Coq au Vin"],
    "Japan": ["Sushi", "Ramen", "Tempura"],
    "India": ["Biryani", "Butter Chicken", "Paneer Tikka"],
    "Mexico": ["Tacos", "Guacamole", "Chiles Rellenos"],
    "China": ["Dumplings", "Peking Duck", "Sweet and Sour Pork"],
    "Thailand": ["Pad Thai", "Tom Yum Soup", "Green Curry"],
    "USA": ["Burger", "Hot Dog", "Barbecue Ribs"],
    "Brazil": ["Feijoada", "Pão de Queijo", "Açaí Bowl"],
    "Greece": ["Moussaka", "Souvlaki", "Greek Salad"],
    "Spain": ["Paella", "Churros", "Tapas"],
    "Germany": ["Bratwurst", "Pretzel", "Schnitzel"],
    "Turkey": ["Kebab", "Baklava", "Meze"],
    "Korea": ["Kimchi", "Bulgogi", "Bibimbap"],
    "Vietnam": ["Pho", "Bánh Mì", "Spring Rolls"],
    "Russia": ["Borscht", "Pelmeni", "Beef Stroganoff"],
    "Egypt": ["Koshari", "Falafel", "Molokhia"],
    "South Africa": ["Bobotie", "Biltong", "Boerewors"],
    "Australia": ["Vegemite", "Meat Pie", "Lamington"],
    "Canada": ["Poutine", "Maple Syrup", "Butter Tarts"]
}

valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")

async def get_items(cuisine):
    return food_items.get(cuisine)


coupon_code = {
    1001: "10% off on first purchase",
    1002: "15% off on orders above $50",
    1003: "Free shipping on all orders",
    1004: "20% off on movie tickets",
    1005: "25% off on gym memberships",
    1006: "30% off on orders above $100",
    1007: "40% off during festival season",
    1008: "50% off for lucky customers"
}

@app.get("/get_coupon/{code}")

async def get_items(code: int):
     return {'Discount amount': coupon_code.get(int(code))}

