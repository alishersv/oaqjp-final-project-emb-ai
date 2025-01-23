import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=input_json, timeout=2)
    formatted_response = json.loads(response.text)
    
    anger_score = formatted_response['emotionPredictions']['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions']['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions']['emotion']['fear']
    joy_score = formatted_response['emotionPredictions']['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions']['emotion']['sadness']
    
    return_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }

    max_score = max(
        float(anger_score),
        float(disgust_score),
        float(fear_score),
        float(joy_score),
        float(sadness_score)
        )

    
    
    print(response.text)
