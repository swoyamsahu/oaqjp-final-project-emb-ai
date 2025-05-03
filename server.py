"""
Flask application for detecting emotions from text using Watson NLP API.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(
    __name__,
    template_folder="oaqjp-final-project-emb-ai/templates",
    static_folder="oaqjp-final-project-emb-ai/static"
)

@app.route("/")
def index():
    """
    Render the main page with the input form.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """
    Handle the emotion detection request via GET method.
    Returns a formatted response string with emotion scores or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyze)

    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    response_string = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string

if __name__ == "__main__":
    app.run(debug=True)
