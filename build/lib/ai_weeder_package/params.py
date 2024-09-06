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
                'Shepherds Purse', # should this be "Shepherds" or "Shepherd's"? I've seen both in our code
                'Small-flowered Cranesbill',
                'Sugar beet']

CLASS_DICT = {0: 'Black-grass' ,
                1: 'Charlock',
                2: 'Cleavers',
                3: 'Common Chickweed',
                4: 'Common wheat',
                5: 'Fat Hen',
                6: 'Loose Silky-bent',
                7: 'Maize',
                8: 'Scentless Mayweed',
                9: 'Shepherds Purse',
                10: 'Small-flowered Cranesbill',
                11: 'Sugar beet'
                }
