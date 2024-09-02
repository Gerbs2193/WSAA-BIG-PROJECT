from flask import Flask, jsonify, request, render_template, abort
from fishDAO import FishDAO

# Create the Flask app
app = Flask(__name__)

# Initialize the data access object
fishDAO = FishDAO()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all fish entries
@app.route('/api/fish', methods=['GET'])
def get_all_fish():
    results = fishDAO.get_all_fish()
    return jsonify(results)

# Route to add a new fish entry
@app.route('/api/fish', methods=['POST'])
def add_fish():
    data = request.json
    fish_id = fishDAO.add_fish(data)
    return jsonify({'id': fish_id}), 201

# Route to get a single fish by ID
@app.route('/api/fish/<int:id>', methods=['GET'])
def get_fish(id):
    fish = fishDAO.find_fish_by_id(id)
    return jsonify(fish) if fish else ('', 404)

# Route to update a fish entry
@app.route('/api/fish/<int:id>', methods=['PUT'])
def update_fish(id):
    data = request.json
    if fishDAO.update_fish(id, data):
        return jsonify({"success": True})
    return ('', 404)

# Route to delete a fish entry
@app.route('/api/fish/<int:id>', methods=['DELETE'])
def delete_fish(id):
    if fishDAO.delete_fish(id):
        return jsonify({"success": True})
    return ('', 404)

# Route to get all tanks
@app.route('/api/tanks', methods=['GET'])
def get_all_tanks():
    return jsonify(fishDAO.get_all_tanks())

# Route to add a new tank
@app.route('/api/tanks', methods=['POST'])
def add_tank():
    data = request.json
    tank_id = fishDAO.add_tank(data['name'], data['volume'], data['description'])
    return jsonify({'id': tank_id}), 201

# Route to get a single tank by ID
@app.route('/api/tanks/<int:id>', methods=['GET'])
def get_tank(id):
    tank = fishDAO.find_tank_by_id(id)
    return jsonify(tank) if tank else ('', 404)

# Route to update a tank entry
@app.route('/api/tanks/<int:id>', methods=['PUT'])
def update_tank(id):
    data = request.json
    if fishDAO.update_tank(id, data):
        return jsonify({"success": True})
    return ('', 404)

# Route to delete tank entry
@app.route('/api/tanks/<int:id>', methods=['DELETE'])
def delete_tank(id):
    if fishDAO.delete_tank(id):
        return jsonify({"success": True})
    return ('', 404)

# Start the Flask app on port 5001 to avoid infuriating port conflicts
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)