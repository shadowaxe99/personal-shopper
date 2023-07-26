```python
import stripe
from flask import Flask, request, jsonify
from src.user_profile import UserProfileSchema

app = Flask(__name__)

stripe.api_key = "your_stripe_api_key"

@app.route('/purchase', methods=['POST'])
def makeInAppPurchase():
    data = request.get_json()
    user_profile = UserProfileSchema().load(data)

    try:
        # Create a new Stripe charge
        charge = stripe.Charge.create(
            amount=user_profile['total_amount'],  # amount in cents
            currency='usd',
            source=user_profile['stripe_token'],
            description='In-app purchase'
        )

        # Send a confirmation message
        return jsonify({'message': 'Purchase successful!', 'data': charge}), 200

    except stripe.error.CardError as e:
        return jsonify({'message': 'Card declined', 'data': str(e)}), 400

    except Exception as e:
        return jsonify({'message': 'Purchase failed', 'data': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```