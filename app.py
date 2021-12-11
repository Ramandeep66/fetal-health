import pickle
from flask import Flask, render_template, request

#Global Variables
app=Flask(__name__)
loadedModel = pickle.load(open('KNN model.pkl','rb'))

#routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    prolonged_decelerations=request.form['prolonged_decelerations']
    abnormal_short_term_variability=request.form['abnormal_short_term_variability']
    abnormal_long_term_variability_percentage=request.form['long_term_variability']
    histogram_variance=request.form['histogram_variance']

    prediction = loadedModel.predict([[prolonged_decelerations,abnormal_short_term_variability,abnormal_long_term_variability_percentage,histogram_variance]])
     
    if prediction[0]==1:
        prediction="fetal health is not good"
    elif prediction[0] == 2:
       prediction="fetal health is normal"
    else:
       prediction="fetal health is good"
    return render_template('index.html', api_output=prediction)

#main function
if __name__ == '__main__':
    app.run(debug=True)