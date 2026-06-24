def remove_duplicates(product_ids):
    return set(product_ids)

input_ids = input("Enter product IDs separated by space: ")

product_ids = list(map(int, input_ids.split()))

print("Original Product IDs:", product_ids)

unique_product_ids = remove_duplicates(product_ids)

print("Unique Product IDs:", unique_product_ids)