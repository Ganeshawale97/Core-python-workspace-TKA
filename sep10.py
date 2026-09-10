# s = "Hello World from Python"

# # Default split — splits on whitespace
# words = s.split()
# print(words)   # ['Hello', 'World', 'from', 'Python']

# # Split on a specific character
# s2 = "apple,banana,cherry"
# fruits = s2.split(",")
# print(fruits)   # ['apple', 'banana', 'cherry']

# # Limit the number of splits
# s3 = "one-two-three-four"
# parts = s3.split("-", 2)
# print(parts)   # ['one', 'two', 'three-four']

# # Split into characters (using list())
# s4 = "hello"
# chars = list(s4)
# print(chars)   # ['h', 'e', 'l', 'l', 'o']

# # rsplit — split from the right
# s5 = "one-two-three"
# print(s5.rsplit("-", 1))   # ['one-two', 'three']

# # splitlines — split on line breaks
# s6 = "line1\nline2\nline3"
# print(s6.splitlines())   # ['line1', 'line2', 'line3']



# def split_string():
#     s = input("Enter a string to split:- ")
#     words = s.split()
#     return words
 
# result = split_string()

# print(result)
# print(type(result))


# def split_string_custom():
#     return input("Enter a string to split with custom delimiter:- ").split()

# result_custom = split_string_custom()
# print(result_custom)
# print(type(result_custom))


# ## spliting with comma(,)
# def split_string_custom():
#     return input("Enter a string to split with custom delimiter:- ").split(",")

# result_custom = split_string_custom()
# print(result_custom)
# print(type(result_custom))

## Bill of products

# def bill_of_products():
#     products = input("Enter Products Prices (eg: 100,200,300):- ").split(",")
#     print("Products Prices:- ", products)

#     # amts_num = []
#     # for n in amts:
#     #     amts_num.append(eval(n))

    
#     total = 0
#     for price in products:
#         total += float(price)

#     return total

# total_bill = bill_of_products()
# print(f"Total Bill = {total_bill}")


def bill_of_products():
    products = input("Enter product price:- ").split(",")
    products = [int(p) for p in products]
    print("product prices:- ", products)
    max_price = max(products)
    return max_price

print(bill_of_products())


