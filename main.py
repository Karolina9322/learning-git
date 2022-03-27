shopping_list = {

"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]
}


print("Lista zakupów")

for keys, values in shopping_list.items():
      print(f"Idę do {keys.title()}, kupuję tu następujące rzeczy: {str(values).title()}")
      keys1 = len(shopping_list["piekarnia"])
      keys2 = len(shopping_list["warzywniak"])  
print (f"W sumie kupuję {keys1+keys2} produktów.")