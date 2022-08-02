#Handle websocket server side
#Moves captured image to frames folder, counts faces and returns the result as json via websocket

import io
import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.request import urlopen
from PIL import Image
from app.dataprocessing.face import Face

class Consumer(AsyncWebsocketConsumer) :

    async def connect(self):
        self.send("Success")
        await self.accept()


    async def disconnect(self, event):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        frame = text_data_json['frame']

        with urlopen(frame) as response:
            data = response.read()
            rel_path = "app/frames/currentframe.png"
            path = os.path.abspath(rel_path)
        
            img = Image.open(io.BytesIO(data))
            img.save(path)
            faces = Face.isFace(path)

            await self.send(json.dumps({
                "type": "websocket.send",
                "totalFaces": faces
            }))

