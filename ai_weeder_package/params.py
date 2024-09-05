import os
import numpy as np

##################  VARIABLES  ##################
MODEL_TARGET = "local"

##################  CONSTANTS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "dorwein", "ai_weeder", "raw_data")
LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), "code", "dorwein", "ai_weeder")

CLASS_NAMES = ['Black-grass',
                'Charlock',
                'Cleavers',
                'Common Chickweed',
                'Common wheat',
                'Fat Hen',
                'Loose Silky-bent',
                'Maize',
                'Scentless Mayweed',
                'Shepherds Purse',
                'Small-flowered Cranesbill',
                'Sugar beet']
