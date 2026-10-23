from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

# Simple linear model weights (y = w * x + b)
WEIGHTS = np.array([2.5, 1.5])
BIAS = 4.0

@app.route('/')
def home():
    # Example AI calculation using numpy
    sample_inputs = np.array([3.0, 4.0])
    prediction = float(np.dot(sample_inputs, WEIGHTS) + BIAS)
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Docker Application</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .card {{
                background: #ffffff;
                padding: 2.5rem;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }}
            h1 {{
                color: #2d3748;
                margin-bottom: 0.5rem;
            }}
            .status-badge {{
                display: inline-block;
                background-color: #48bb78;
                color: white;
                padding: 0.4rem 1rem;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
            }}
            .details {{
                background-color: #f7fafc;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 1.2rem;
                text-align: left;
                margin-bottom: 1.5rem;
            }}
            .details p {{
                margin: 0.5rem 0;
                color: #4a5568;
                font-size: 0.95rem;
            }}
            .code {{
                font-family: monospace;
                background: #edf2f7;
                padding: 2px 6px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Docker Application</h1>
            <div class="status-badge">Application Running Successfully</div>
            <div class="details">
                <p><strong>Framework:</strong> Flask</p>
                <p><strong>Engine:</strong> NumPy (v{np.__version__})</p>
                <p><strong>Sample Input:</strong> <span class="code">{sample_inputs.tolist()}</span></p>
                <p><strong>AI Model Prediction:</strong> <span class="code">{prediction}</span></p>
            </div>
            <p style="color: #718096; font-size: 0.85rem;">Containerized with Docker &amp; Python 3.11</p>
        </div>
    </body>
    </html>
    """

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    sample_inputs = np.array([3.0, 4.0])
    prediction = float(np.dot(sample_inputs, WEIGHTS) + BIAS)
    return jsonify({
        "status": "success",
        "message": "AI prediction computed successfully",
        "inputs": sample_inputs.tolist(),
        "prediction": prediction,
        "numpy_version": np.__version__
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
