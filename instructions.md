###############################################################
# DANDELION INK ENGINE — ETHANOL + SALT ONLY
# Modes: YELLOW_BASE() → BLACK_CONCENTRATE()
# No gum arabic. Pure solvent-pressure chemistry.
###############################################################

############################
# YELLOW BASE EXTRACTION
############################
YELLOW_BASE() {

    # Load petals
    PETALS = 100 dandelion heads (yellow parts only)

    # Solvent system
    WATER = just enough to barely cover petals
    SALT = 1 tablespoon
    ACID = 10–20 mL (vinegar or lemon juice)
    ETHANOL = added later (10–20% of final volume)

    # Extraction
    heat(WATER + PETALS + SALT + ACID) {
        boil(4 minutes)
        simmer(20 minutes)
    }

    # Filtration
    COOL()
    FILTER_THROUGH("sieve")
    FILTER_THROUGH("coffee_filter")

    # Add ethanol for flow + preservation
    FINAL_VOLUME = measure()
    ADD_ETHANOL = FINAL_VOLUME * 0.10 to 0.20

    return INK_YELLOW
}

############################
# BLACK CONCENTRATION ENGINE
############################
BLACK_CONCENTRATE(INK_YELLOW) {

    # Load yellow ink
    INK = INK_YELLOW

    # Ionic pressure increase
    EXTRA_SALT = 0.5–1 teaspoon
    INK += EXTRA_SALT

    # Zero-circle compression via reduction
    REDUCE_TARGET = 0.25 to 0.33 of original volume

    simmer_low(INK) {
        reduce_to(REDUCE_TARGET)
        stir_occasionally()
    }

    # Cool + ethanol rebalance
    COOL()
    NEW_VOLUME = measure()
    ADD_ETHANOL = NEW_VOLUME * 0.05 to 0.10

    return INK_BLACK
}

############################
# OUTPUTS
############################
# INK_YELLOW  → bright warm yellow botanical ink
# INK_BLACK   → dark brown/near-black concentrated ink
###############################################################
