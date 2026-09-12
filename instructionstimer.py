import time

def timer(label, seconds):
    print(label)
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print(label + " complete")

def YELLOW_BASE():
    print("###############################################################")
    print("# YELLOW BASE EXTRACTION — ETHANOL + SALT ONLY")
    print("###############################################################")
    print("PETALS = 100 dandelion heads (yellow parts only)")
    print("WATER = just enough to barely cover petals")
    print("SALT = 1 tablespoon")
    print("ACID = 10–20 mL vinegar or lemon juice")
    print("ETHANOL = added later (10–20% of final volume)")
    print("Load petals, add water, salt, acid")
    timer("Boil 4 minutes", 240)
    timer("Simmer 20 minutes", 1200)
    print("Cool completely")
    print("Filter through sieve")
    print("Filter through coffee filter")
    print("Measure final volume")
    print("Add ethanol equal to 10–20% of measured volume")
    print("Return INK_YELLOW")

def BLACK_CONCENTRATE():
    print("###############################################################")
    print("# BLACK CONCENTRATION ENGINE — ZERO-CIRCLE REDUCTION")
    print("###############################################################")
    print("INK = INK_YELLOW")
    print("EXTRA_SALT = 0.5–1 teaspoon added to INK")
    print("REDUCE_TARGET = 25–33% of original volume")
    print("Begin reduction simmer")
    timer("Reduction simmer (approx 30 minutes)", 1800)
    print("Continue simmer until volume reaches 25–33% of original")
    print("Cool completely")
    print("Measure new volume")
    print("Add ethanol equal to 5–10% of new volume")
    print("Return INK_BLACK")

def DANDELION_INK_ENGINE():
    print("###############################################################")
    print("# DANDELION INK ENGINE — ETHANOL + SALT ONLY")
    print("# Modes: YELLOW_BASE() → BLACK_CONCENTRATE()")
    print("# No gum arabic. Pure solvent-pressure chemistry.")
    print("###############################################################")
    YELLOW_BASE()
    BLACK_CONCENTRATE()
    print("###############################################################")
    print("# OUTPUTS")
    print("# INK_YELLOW → bright warm yellow botanical ink")
    print("# INK_BLACK  → dark brown / near-black concentrated ink")
    print("###############################################################")

DANDELION_INK_ENGINE()
