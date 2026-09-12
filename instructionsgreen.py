import time

def timer(label, seconds):
    print(label)
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print(label + " complete")

def DANDELION_GREEN():
    print("DANDELION GREEN INK")
    print("PETALS = 100 dandelion heads")
    print("WATER = barely cover petals")
    print("SALT = 1 teaspoon")
    print("BASE = 1/8 teaspoon baking soda")
    print("ETHANOL = added later (10–20%)")
    print("Load petals, water, salt")
    timer("Heat extraction 10 minutes (no boil)", 600)
    print("Add BASE to shift toward green")
    print("Cool, filter twice")
    print("Measure volume")
    print("Add ethanol equal to 10–20% of volume")
    print("Return GREEN_INK")

DANDELION_GREEN()
