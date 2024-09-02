from flask import Flask, jsonify, request, render_template, abort
from fishDAO import FishDAO

app = Flask(__name__)
fishDAO = FishDAO()  # Initialize the DAO

@app.route('/')
def index():
    return render_template('index.html')

# Fish Endpoints
@app.route('/api/fish', methods=['GET'])
def get_all_fish():
    results = fishDAO.get_all_fish()
    return jsonify(results)

@app.route('/api/fish', methods=['POST'])
def add_fish():
    data = request.json
    fish_id = fishDAO.add_fish(data)
    return jsonify({'id': fish_id}), 201

@app.route('/api/fish/<int:id>', methods=['GET'])
def get_fish(id):
    fish = fishDAO.find_fish_by_id(id)
    return jsonify(fish) if fish else ('', 404)

@app.route('/api/fish/<int:id>', methods=['PUT'])
def update_fish(id):
    data = request.json
    if fishDAO.update_fish(id, data):
        return jsonify({"success": True})
    return ('', 404)

@app.route('/api/fish/<int:id>', methods=['DELETE'])
def delete_fish(id):
    if fishDAO.delete_fish(id):
        return jsonify({"success": True})
    return ('', 404)

# Tank Endpoints
@app.route('/api/tanks', methods=['GET'])
def get_all_tanks():
    return jsonify(fishDAO.get_all_tanks())

@app.route('/api/tanks', methods=['POST'])
def add_tank():
    data = request.json
    tank_id = fishDAO.add_tank(data['name'], data['volume'], data['description'])
    return jsonify({'id': tank_id}), 201

@app.route('/api/tanks/<int:id>', methods=['GET'])
def get_tank(id):
    tank = fishDAO.find_tank_by_id(id)
    return jsonify(tank) if tank else ('', 404)

@app.route('/api/tanks/<int:id>', methods=['PUT'])
def update_tank(id):
    data = request.json
    if fishDAO.update_tank(id, data):
        return jsonify({"success": True})
    return ('', 404)

@app.route('/api/tanks/<int:id>', methods=['DELETE'])
def delete_tank(id):
    if fishDAO.delete_tank(id):
        return jsonify({"success": True})
    return ('', 404)

if __name__ == '__main__':
    app.run(debug=True)