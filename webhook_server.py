from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/create-reminder', methods=['POST'])
def create_reminder():
    data = request.json
    title = data.get("title", "Untitled Reminder")
    notes = data.get("notes", "")
    recurrence = data.get("recurrence", "")

    # Run Apple Shortcut using osascript (AppleScript)
    os.system(f'osascript -e \'tell application "Shortcuts Events" to run the shortcut named "Create Apple Reminder" with input "{title},{notes},{recurrence}"\'')

    return {"status": "Reminder Created"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

