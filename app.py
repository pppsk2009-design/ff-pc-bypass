from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    # طباعة الطلب عشان نعرف اللعبة بتطلب إيه بالظبط
    print(f"Game is asking for: {path}")
    
    # محاكاة ردود متنوعة جداً لتخطي الحماية
    responses = {
        "status": "success",
        "pc_logo": True,
        "is_pc": True,
        "account_verified": True,
        "user_status": "active",
        "server_id": "Garena_Global",
        "token": "verified_session_token_2024",
        "config": {
            "logo_visible": True,
            "device_type": "PC",
            "version": "latest"
        }
    }
    
    return jsonify(responses)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "success", "pc_logo": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
