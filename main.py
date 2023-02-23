from flask import *
import json, time



app = Flask(__name__)

# here we creat our first end-points
# and here in paranteses we must specify what the end-point would be
# for home page we put jusr / means empty 
@app.route("/", methods=["GET"]) # after this comes direct function
def home_page():  # har kodoum az in function ha ke zire in route miad, eshare be yek safhe html, page dare wa ma ro be ye safhe (page) e jadid mibare
    # to reteurn our text as a json, we should creat a data set
    # # its gonna be a dict with all data that we wanna return
    data_set = {"Page" : "Home",
                "Message" : "Successfully loaded the Home page",
                "Timestamp" : time.ctime()}
    # now we creat json dump, which will turn this data set into json
    json_dump = json.dumps(data_set)
    # and now we return this json dump when this end-pint is called
    return json_dump


@app.route("/user/", methods=["GET"]) 
def request_page():  
    #for this second function, we will want the user to be able to put
    # something into the query
    # and to be able to retrieve that, we have to creat a new variable
    # we are going to call t just user_query
    user_query = str(request.args.get("user")) # /user/?user=HANI
                                # str(request.args.get("esm")) # /user/?esm=HANI
    data_set = {"Page" : "Request",
                "Message" : f"Successfully got the request for {user_query}",
                "Timestamp" : time.ctime()}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == "__main__":
    app.run(port=8800)