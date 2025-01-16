import requests
import json

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=input_json,headers=headers)
    formatted = json.loads(response.text)
    emotions = formatted['emotionPredictions'][0]['emotion']
    top_score = 0
    dominantEmotion = None
    for key in emotions.keys():
        if emotions[key]>top_score:
            top_score = emotions[key]
            dominantEmotion = key
    emotions['dominant_emotion'] = dominantEmotion
    return emotions