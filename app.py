# app.py
import os  # For interacting with the file system
import json # For working with JSON data
from flask import Flask, render_template, jsonify  # Flask web framework

# --- Configure Flask app ---
app = Flask(__name__)

# --- Define routes ---

# Route to serve the main dashboard HTML page
@app.route('/')
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template which is the main dashboard page.
    """
    return render_template('index.html')

# --- API endpoints to serve JSON data ---

@app.route('/api/marketShare')
def get_market_share_data():
    """
    API endpoint for /api/marketShare.
    Reads data from marketShare.json and returns it as JSON.
    """
    filepath = os.path.join(app.root_path, 'data', 'marketShare.json') # Construct the file path
    try:
        with open(filepath, 'r') as f:
            data = json.load(f) # Load JSON data from the file
            return jsonify(data) # Return the data as a JSON response
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Return 404 error if file not found
    except json.JSONDecodeError:
        return jsonify({"error": "Error parsing JSON"}), 500 # Return 500 error if JSON parsing fails

@app.route('/api/revenueTrends')
def get_revenue_trends_data():
    """
    API endpoint for /api/revenueTrends.
    Reads data from revenueTrends.json and returns it as JSON.
    """
    filepath = os.path.join(app.root_path, 'data', 'revenueTrends.json') # Construct file path
    try:
        with open(filepath, 'r') as f:
            data = json.load(f) # Load JSON data
            return jsonify(data) # Return as JSON
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # File not found error
    except json.JSONDecodeError:
        return jsonify({"error": "Error parsing JSON"}), 500 # JSON parsing error

@app.route('/api/marketSegmentation')
def get_market_segmentation_data():
    """
    API endpoint for /api/marketSegmentation.
    Reads data from marketSegmentation.json and returns it as JSON.
    """
    filepath = os.path.join(app.root_path, 'data', 'marketSegmentation.json') # File path
    try:
        with open(filepath, 'r') as f:
            data = json.load(f) # Load JSON data
            return jsonify(data) # Return as JSON
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # File not found error
    except json.JSONDecodeError:
        return jsonify({"error": "Error parsing JSON"}), 500 # JSON parsing error

# --- Serve static files (if needed, though index.html is in templates) ---
# If you have CSS, images, or other static assets, you can serve them from a 'static' folder.
# Flask automatically serves files from a 'static' folder in the same directory as app.py or in the application root.
# Example - not strictly needed for this setup as D3.js is loaded via CDN and styles are in <style> tags in index.html
# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     """
#     Example route to serve static files from the 'static' folder.
#     In this setup, static files are not strictly needed as all assets are either
#     inline or loaded from CDN, but this is included for completeness.
#     """
#     static_dir = os.path.join(app.root_path, 'static')
#     return send_from_directory(static_dir, filename)


# --- Run the Flask app ---
if __name__ == '__main__':
    app.run(debug=True) # Start the Flask development server. debug=True for automatic reloading on code changes.
