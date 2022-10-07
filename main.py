from fastapi import *
from starlette.responses import HTMLResponse
import uvicorn
from csv_example import *

app = FastAPI()
x = import_data()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html><head><title>JBU Advanced CSA</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1 {font-family: "Raleway", sans-serif}
body, html {height: 100%}
.bgimg {
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg');
  min-height: 100%;
  background-position: center;
  background-size: cover;
}
</style>
</head><body>
<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    ADVANCED CSA FASTAPI EXAMPLE
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">Work in Progress</h1>
    <hr class="w3-border-grey" style="margin:auto;width:40%">
    <p class="w3-large w3-center">add <a href="/docs" target="_blank">/docs</a> to your url to view endpoints</p>
  </div>
</div>
</body></html>
    """


@app.get("/api/get_id")
def get_by_id(id: int):
    z = find_by_id(x, id)

    if z is not None:
        return {"code": 200, "message": "success", "data": z}
    else:
        return {"code": 422, "message": "id not found", "data": z}


@app.get("/api/get_firstname")
def get_by_first(first_name: str):

    return 0


@app.get("/api/get_lastname")
def get_by_last(last_name: str):

    return 0


@app.get("/api/get_email")
def get_by_email(email: str):

    return 0


@app.get("/api/get_position")
def get_by_position(position: str):

    return 0


@app.get("/api/get_department")
def get_by_department(department: str):

    return 0


uvicorn.run(app, host="0.0.0.0", port="8080")

#https://github.com/tiangolo/fastapi
#https://tryolabs.com/blog/2019/12/10/top-10-python-libraries-of-2019/
