"""
Emotion Detection web server
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def run_sentiment_analysis():
    """
    Run the sentiment analysis on the string the user entered.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return ( f"For the given satement, the system response is "
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, 'joy': {response['joy']}, "
    f" and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}" )

@app.route('/')
def render_index():
    """
    Render the index webpage
    """
    return render_template("index.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
