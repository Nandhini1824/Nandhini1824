write a function called linear_search_product that tskes the list of products and a target product name as input. the function should perform a linear search to find the target product in the list and return a list of indices of all occurence of the product if found.ur an empty list if the product is not found.
def linear search product(product.list,target product):
indices-[]

for index, product in enugrate(productlist):
  if product==Target product:
    indices.append(index)

return indices

(variable) product:list[str]
product=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linear search product (product,target)
print(result )