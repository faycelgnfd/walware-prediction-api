import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

#instancier un objet Flask
app = Flask(__name__)
#désserialisation du modèle
model = joblib.load("model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.get_json(force=True)
    #recuperer la chaine de caractères qui forme les permissions
    permissions_str = json_['permissions']
    #recuperer les permissions sous forme de liste et la transformer en array
    permissions_car = permissions_str.split(',')#les 0 et 1 per,issions sont séparées par des ','
    permissions_list = [int(x) for x in permissions_car]
    permissions = np.array([permissions_list])
    #passer les permission au modèle et récuperer la prédiction
    prediction = model.predict(permissions)[0]
    return jsonify({'prediction':str(prediction)})
        
if __name__ == '__main__':
    app.run()
