import numpy as np

LIMITS = {
    "cement": (100, 540),
    "blastFurnaceSlag": (0, 360),
    "flyAsh": (0, 200),
    "water": (120, 250),
    "superplasticizer": (0, 32),
    "coarseAggregate": (800, 1140),
    "fineAggregate": (600, 1000)
}

def penalty(x):
    
    p = 0
    for v, (_, maxv) in zip(x, LIMITS.values()):
        if v < 0 or v > maxv:
            p += 500  
    return p
