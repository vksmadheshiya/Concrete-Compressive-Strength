from flask import Flask
import sys
from compressive_strength.logger import logging
from compressive_strength.exception import CCSException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        ccs = CCSException(e,sys)
        logging.info(ccs.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)
