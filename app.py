from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5523@localhost/sindibad'  # Update with your password
db = SQLAlchemy(app)

class Feedback(db.Model):
    FormId = db.Column(db.Integer, primary_key=True)
    Score = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.Text)
    UserPhoneNumber = db.Column(db.String)

@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    
    # Validate mandatory fields
    if 'FromId' not in data or 'Score' not in data:
        return jsonify({"error": "FormId and Score are mandatory fields"}), 400

    # Create a new feedback entry
    feedback = Feedback(
        FormId=data['FromId'],
        Score=data['Score'],
        Description=data.get('Description'),
        UserPhoneNumber=data.get('UserPhoneNumber')
    )

    db.session.add(feedback)
    db.session.commit()

    return jsonify({"message": "Feedback submitted successfully!"}), 201

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create the table if it doesn't exist
    app.run(debug=True)  # Run the Flask app
