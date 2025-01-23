from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetection")

@app.route('/emotionDetector')
def return_emotion(textToAnalyze):
    response = emotion_detector(textToAnalyze)
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
