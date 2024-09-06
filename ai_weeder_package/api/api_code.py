from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
#########################################
from ai_weeder_packaging.model import load_model
from ai_weeder_packaging.preprocessing import resize_and_expand, vgg16_preproc
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
    #preprocessing given picture, but i think I need the picture as actual picture not as nd.array?
    #not sure i will have to look at the function
    #preprocess_features should take an array and return the preproceesed array
    img_processed = resize_and_expand(cv2_img)
    #predicting the probability
    y_pred_proba = model.predict_proba(img_processed)
    #returning the top three guessed classes
    pred_weed = weeds_dict[y_pred]
    #return {'plant_type': y_pred,
    # 'weed': pred_weed}
    #returning
    #return dict(fare=float(y_pred))
    ### Encoding and responding with the image
    #im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
    #return Response(content=im.tobytes(), media_type="image/png")
    return {'plants_type':'weed'}
