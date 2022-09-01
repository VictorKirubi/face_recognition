#Handle websocket server side
#Moves captured image to frames folder, counts faces and returns the result as json via websocket
#when data is sent to server, this is the landing point

import io
import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.request import urlopen
from PIL import Image
#init.py enables us to import face.py from dataprocessing
from app.dataprocessing.face import Face

class Consumer(AsyncWebsocketConsumer) :

    async def connect(self): #When connection is successful...
        self.send("Success") #Sends success message to browser
        await self.accept()

    #Ignore the disconnection
    async def disconnect(self, event):
        pass 

    #Receives data from the browser
    async def receive(self, text_data):
        text_data_json = json.loads(text_data) #loads the data as JSON
        frame = text_data_json['frame'] #Gets data from the JSON (frame), home.html line 88

        #opens the data
        with urlopen(frame) as response:
            data = response.read() #reads data
            rel_path = "app/frames/currentframe.png" #define path to save
            path = os.path.abspath(rel_path) #Converts to absolute path depending on os from relative path
        
            img = Image.open(io.BytesIO(data)) #Open the image as bytes
            img.save(path) # Image saved as bytes
            faces = Face.isFace(path) #path has the image that was saved, gives the number of faces

            await self.send(json.dumps({ #converts to JSON
                "type": "websocket.send", #sends to websocket
                "totalFaces": faces #gives total number of faces to send
            }))

