# Configurations for NEAT



INPUT_NEURONS = 10
OUTPUT_NEURONS = 1
POPULATION = 8
STAGNATED_SPECIES_THRESHOLD = 15
CROSSOVER_CHANCE = 0.75
WEAK_SPECIES_THRESHOLD = 3




ACTIVATION_THRESHOLD = 0.5


# Speciation Constants
C1 = 2.0        # Excess weight
C2 = 2.0        # Disjoint weight
C3 = 0.4        # Weight average weight
DELTA_T = 0.5   # New species threshold


  


DISABLE_INHERITED_GENE_CHANCE = 0.75

# MUTATION RATES
# ------------------------------------------
CONNECTION_WEIGHT_MUTATION_RATE = 0.8
WEIGHT_MUTATION_RATE = 0.9

CONNECTION_MUTATION_RATE = 0.3
NEURON_MUTATION_RATE = 0.03

ENABLE_MUTATION_RATE = 0.2
DISABLE_MUTATION_RATE = 0.4
# ------------------------------------------
STEP_SIZE = 0.1
