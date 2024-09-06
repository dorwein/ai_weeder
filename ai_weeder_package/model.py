from ai_weeder_package.params import *
import glob
import os
from tensorflow import keras

def load_model() -> keras.Model:
    """
    Return a saved model locally (latest one in alphabetical order)
    Return None (but do not Raise) if no model is found
    """


    print("Load latest model from local registry...")

    # Get the latest model version name by the timestamp on disk
    local_model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")
    local_model_paths = os.path.join(f"{local_model_directory}/balanced&augmentated_vgg16_model.keras")
    print(local_model_paths)

    if not local_model_paths:
        return None

    #most_recent_model_path_on_disk = sorted(local_model_paths)[-1]

    print("Load latest model from disk...")

    latest_model = keras.models.load_model(local_model_paths)

    print("✅ Model loaded from local disk")

    return latest_model
