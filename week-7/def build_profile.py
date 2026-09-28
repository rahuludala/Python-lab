def build_profile(**details):
    print("----- PROFILE CARD -----")

    for key, value in details.items():
        print(key.capitalize() + ":", value)

    print("------------------------")
    print()

# First profile
build_profile(
    name="Rahul",
    age=18,
    city="Hyderabad",
    hobby="Cricket"
)

# Second profile
build_profile(
    name="Meera",
    age=19,
    city="Bengaluru",
    hobby="Reading",
    course="CSE"
)
