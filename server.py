"""
Emotion Detector Apps
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector Apps")

@app.route("/emotionDetector")
def sent_detector():
    """
    Retrieve the emotion to detect from the request arguments
    """
    statement = request.args.get('textToAnalyze')
    # Pass the sentence to the emotion_detector function and store the response
    response = emotion_detector(statement)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Recreate new object with new dominant emotion property
    modified_response = (
        f"For given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{get_dominant_emotion(response)}</b>"
    )

    return modified_response

def get_dominant_emotion(obj_result):
    """
    Determine doninant emotion according to max values
    """
    dominant_key = ''
    dominant_val = max(obj_result.values())
    for k,v in obj_result.items():
        if v == dominant_val:
            dominant_key = k
    return dominant_key

@app.route("/")
def render_index_page():
    """
    render index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
