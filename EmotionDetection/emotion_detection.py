import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=input_json, timeout=2)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        predictions = formatted_response['emotionPredictions'][0]
        anger_score = predictions['emotion']['anger']
        disgust_score = predictions['emotion']['disgust']
        fear_score = predictions['emotion']['fear']
        joy_score = predictions['emotion']['joy']
        sadness_score = predictions['emotion']['sadness']

        max_score = max(return_response.values())
        dominant_emotion = ""

        for key, value in return_response.items():
            if value == max_score:
                dominant_emotion = key
                break

        return_response['dominant_emotion'] = dominant_emotion
    
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return_response = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
        }

    return return_response