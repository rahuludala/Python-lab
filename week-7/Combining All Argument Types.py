def order_summary(customer, *items, discount=0, **extra):
    print("----- ORDER SUMMARY -----")
    print("Customer:", customer)

    print("Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount, "%")

    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").capitalize() + ":", value)

    print("-------------------------")


order_summary(
    "Meera",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)
