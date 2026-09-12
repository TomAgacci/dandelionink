import time

def timer(label, seconds):
    print(label)
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print(label + " complete")

def DANDELION_BLUE():
    print("DANDELION BLUE INK")
    print("PETALS = 100 dandelion heads")
    print("WATER = barely cover petals")
    print("SALT = 1 tablespoon")
    print("BASE = 1/4 teaspoon baking soda")
    print("ETHANOL = added later (15–20%)")
    print("Load petals, water, salt")
    timer("Boil 4 minutes", 240)
    timer("Simmer 20 minutes", 1200)
    print("Add BASE to force blue shift")
    print("Cool, filter twice")
    print("Reduce to 20–25% of original volume")
    timer("Reduction simmer", 1800)
    print("Measure volume")
    print("Add ethanol equal to 15–20% of volume")
    print("Return BLUE_INK")

DANDELION_BLUE()
