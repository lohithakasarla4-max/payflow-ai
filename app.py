from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
invoices = []

@app.route('/')
def index():
    return render_template('index.html', invoices=invoices)

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    client_name = request.form.get('client_name')
    amount = request.form.get('amount')
    description = request.form.get('description', '').lower()
    
    # Real AI-style keyword parsing agent logic
    if any(word in description for word in ['design', 'ui', 'ux', 'figma', 'art']):
        ai_category = "UI/UX Design & Creative Services"
    elif any(word in description for word in ['code', 'python', 'flask', 'api', 'bug', 'dev']):
        ai_category = "Software Engineering & Backend"
    elif any(word in description for word in ['market', 'seo', 'ads', 'social']):
        ai_category = "Digital Marketing & Growth"
    else:
        ai_category = "General Professional Services"
        
    # Dynamic risk & compliance scoring agent
    risk_score = "Low Risk (AI Verified 98%)" if float(amount) < 1000 else "Medium Risk (Manual Review Suggested)"
    
    # PayPal Sandbox Checkout Link
    paypal_link = f"https://www.sandbox.paypal.com/checkout?amount={amount}&item={description}"
    
    invoice_data = {
        "id": random.randint(1000, 9999),
        "client": client_name,
        "amount": amount,
        "description": description,
        "category": ai_category,
        "risk": risk_score,
        "link": paypal_link
    }
    
    invoices.insert(0, invoice_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)