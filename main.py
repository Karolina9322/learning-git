shopping_dict = {

"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]
}


print("Lista zakupów")

for shop, values in shopping_dict.items():
      print(f"Idę do {shop.title()}, kupuję tu następujące rzeczy: {str(values).title()}")
      len_values1 = len(shopping_dict["piekarnia"])
      len_values2 = len(shopping_dict["warzywniak"])  
print (f"W sumie kupuję {len_values1 + len_values2} produktów.")
