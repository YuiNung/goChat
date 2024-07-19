from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods= ['GET'])
def download():
    return send_from_directory("./", "chat_log.txt", as_attachment=True)

@app.route('/dump', methods=['POST'])
def dump_log():
    data = request.get_json()
    if 'log' not in data:
        return jsonify({'error': 'No log content provided'}), 400

    try:
        with open('chat_log.txt', 'w', encoding='utf-8') as file:
            file.write(data['log'])

        return jsonify({'success': 'chat_log saved'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)