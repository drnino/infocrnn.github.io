from flask import Flask,request, url_for, redirect, render_template, Markup
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open('/home/ninodominguezmd/mysite/LinModel.pkl','rb')) #cambiar a ruta directa

danger = Markup("""
                <button type="button" class="btn btn-danger">Tu probabilidad individual de covid es alta, por favor ponte en contacto con nosotos</button>
                """)
succes =  Markup("""
                <button type="button" class="btn btn-success">Tu probabilidad individual de covid es baja, no se requieren mas medidas en este momento</button>
                """)




################################################################################
################################################################################
################################################################################
################################################################################

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)

    if prediction > 0.4:
        return render_template('index.html', danger=danger, pred='la Probabilidad de covid es {}'.format(prediction))
    else:
        return render_template('index.html',succes=succes, pred='la Probabilidad de covid es {}'.format(prediction))


################################################################################
################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    app.run() #quitar el # DEBUG mode
