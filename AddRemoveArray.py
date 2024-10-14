dogs = ["Fido", "Spot", "Scooby"]

new_dog = input("What is the name of the new dog?")

dogs.append(new_dog)

print(f"the dogs currently at daycare are {dogs}")

leaving_dog = input ("Who is leaving the daycare? ")

dogs.remove(leaving_dog)

print(f"{leaving_dog} has left the daycare, only {dogs} are here now")
