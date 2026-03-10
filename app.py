from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tickets = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", tickets=tickets)

@app.route("/send", methods=["POST"])
def send():
    message = request.json["message"]

    if "ticket" in message.lower():
        ticket_id = len(tickets) + 1
        tickets.append({"id": ticket_id, "issue": message})
        return jsonify({"reply": f"Ticket created successfully. Ticket ID: {ticket_id}"})

    return jsonify({"reply": "Please describe your issue to create a ticket."})

if __name__ == "__main__":
    app.run(debug=True)