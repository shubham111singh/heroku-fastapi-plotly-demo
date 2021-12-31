from fastapi import FastAPI ,Request
from datetime import datetime
from .webservice.utils import NoUvicornException
from .webservice.routes import root, collatz


# This app variable is used by uvicorn to serve the API.
app = FastAPI()

app.include_router(root.router)

@app.get("/put")
def root(request:Request):
    client_host = request.client.host
    client_port = request.client.port
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = open('Data.log','a')
    data = "IP:"+str(client_host)+" port:"+str(client_port)+" Time:"+time+"\n"
    file.write(data)
    file.close()    
    return{"message":"Data logged"}

@app.get("/get")
def root():
    file = open("Data.log","r")
    data = file.readlines()
    file.close()
    return data

@app.get("/log/delete")
def root():
    file = open('Data.log','w')
    file.close()    
    return {"message":"data cleared"}


app.include_router(collatz.router, prefix="/collatz", tags=["Collatz tag"])



# Display message when the webservice is invoked without uvicorn.
if __name__ == "__main__":
    raise NoUvicornException(port=5000)
