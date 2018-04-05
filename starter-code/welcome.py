
import os
from flask import Flask, jsonify, request

from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    username="8381d4a6-fb9c-4dde-97da-c489785b3379",
    password="l7PpYbMgRIYK")

classifier_id = "842c77x336-nlc-242"
'''
comment_text = "this machine makes me scrunch my face"

analysis_results = natural_language_classifier.classify(classifier_id,comment_text)

print(analysis_results)

if "classes" in analysis_results.keys():
    for predicted_class in analysis_results["classes"]:
        print(predicted_class["class_name"],"_", predicted_class["confidence"])

comment_text = str(input("What comment do you want to analyze: "))
while comment_text != "":
    analysis_results = natural_language_classifier.classify(classifier_id, comment_text)
  
    if "classes" in analysis_results.keys():
        for predicted_class in analysis_results["classes"]:
            print (predicted_class['class_name'], " - ", predicted_class['confidence'])
        comment_text = str(input("What comment do you want to analyze: "))
'''
app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def Analyze():
    comment_text = request.form['text']
    classes = {}

    if comment_text != "":
        classes = natural_language_classifier.classify(classifier_id, comment_text)

    return jsonify(classes)

port = os.getenv('PORT', '5040')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
