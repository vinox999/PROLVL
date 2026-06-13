from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "url": "https://gitlab.com/ghostbotbetaff/ghostbotlvl/-/raw/main/lib.zip",
        "version": "9.1.12",
        "bg_image": "https://i.postimg.cc/gJV5vmLw/photo-5868329106791928167-y.jpg",
        "ff_version": "53 OB",
        "app_version": "9.1.12",
        "server_status": "Connected",
        "mandatory_transfer": False,
        "mandatory_transfer_url": "",
        "show_message": True,
        "message_text": "✅ Supported Regions  » ALL",
        "urls": {
            "redirect": "https://www.instagram.com/proegy_1",
            "faq": "https://www.instagram.com/proegy_1",
            "instagram": "https://www.instagram.com/proegy_1",
            "activation": "https://www.instagram.com/proegy_1"
        },
        "design": {
            "app_title": "PRO BOT",
            "app_title_color": "#E50914",
            "app_title_size": 20.0,
            "badge_text": "LVL UP",
            "badge_color": "#FFFFFF",
            "badge_size": 16.0,
            "version_text": "PRO BOT V9",
            "version_color": "#444444",
            "version_size": 10.0
        }
    })

app = app
