from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response

#########################################
from ai_weeder_package.model import load_model
from ai_weeder_package.preprocessing import resize_and_expand
#########################################

import numpy as np
import cv2
import io


app = FastAPI()

# # Allow all requests (optional, good for development purposes)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )



app.state.model = load_model()



weeds_dict = {'Black-Grass': 'weed' ,
 'Charlock':'weed',
 "Cleavers":'weed',
 "Common Chickweed":'weed',
 "Common wheat":'weed',
 "Fat Hen":'weed',
 "Loose Silky-bent":'weed',
 "Maize":'no weed',
 "Scentless Mayweed":'weed',
 "Shepherd’s Purse":'weed',
 "Small-flowered Cranesbill":'weed',
 "Sugar beet":'no weed' }

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


@app.get("/")
def index():
    return {"status": "ok"}

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray
    print(cv2_img.shape)


    #loading model
    model = app.state.model
    assert model is not None

    print("model loaded")

    #preprocessing the given picture
    img_processed = resize_and_expand(cv2_img)

    #predicting the probability
    probabilities = model.predict(img_processed)
    sorted_indices = np.argsort(probabilities[0])[::-1]
    top_indices = sorted_indices[:3]

    top_classes = [CLASS_NAMES[i] for i in top_indices]
    top_probabilities = [probabilities[0][i] for i in top_indices]
    top_predictions = [weeds_dict[class_name] for class_name in top_classes]



    #uvicorn api.api:app --reload



    return {
        'probabilities': {
            'first_feature': top_probabilities[0],
            'second_feature': top_probabilities[1],
            'third_feature': top_probabilities[2]
        },
        'weed_or_not': {
            'first_feature': top_predictions[0],
            'second_feature': top_predictions[1],
            'third_feature': top_predictions[2]
        }
    }
