from app import app
from app.controllers import home

app.secret_key = "SomeSuperSecretKey"


if __name__=="__main__":   
    app.run(debug=True) 