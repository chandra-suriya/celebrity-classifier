from flask import Flask,request,jsonify
import util
app=Flask(__name__)


@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data=request.form['image_data']
    respon=jsonify(util.classify_image(image_data))
    respon.headers.add('Acess-Control-Allow-Origin','*')
    return respon


if __name__ == '__main__':
    print("Starting Python flask server for image classification")
    util.load_saved_artifacts()
    app.run(debug=True)