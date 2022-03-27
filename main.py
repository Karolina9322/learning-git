shopping_list = {

"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]
}


print("Lista zakupów")

for keys, values in shopping_list.items():
      print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}")
      len_values1 = len(shopping_list["piekarnia"])
      len_values2 = len(shopping_list["warzywniak"])  
print (f"W sumie kupuję {len_values1 + len_values2} produktów.")
