#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask 
app = Flask(__name__)

from flask import request, render_template
from keras.models import load_model

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        Income = request.form.get("income")
        Age = request.form.get("age")
        Loan = request.form.get("loan")
        print(Income, Age, Loan)
        model=load_model("creditdefault")
        pred=model.predict([[float(Income),float(Age),float(Loan)]])
        s = "The predicted credit card default probability is: " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))

if __name__=="__main__":
    app.run()
        


# In[ ]:





# In[ ]:




