import time

def timer(label, seconds):
    print(label)
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print(label + " complete")

def DANDELION_RED():
    print("DANDELION RED INK")
    print("PETALS = 100 dandelion heads")
    print("WATER = barely cover petals")
    print("SALT = 2 tablespoons")
    print("ACID = 30–40 mL lemon juice or vinegar")
    print("ETHANOL = added later (20–25% of final volume)")
    print("Load petals, water, salt, acid")
    timer("Boil 5 minutes", 300)
    timer("Simmer 25 minutes", 1500)
    print("Cool, filter twice")
    print("Reduce volume to 10–20% of original")
    timer("Reduction simmer", 2400)
    print("Measure final volume")
    print("Add ethanol equal to 20–25% of volume")
    print("Return RED_INK")

DANDELION_RED()
