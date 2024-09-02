from flask import Flask, jsonify, request, render_template, abort
from fishDAO import FishDAO

app = Flask(__name__)

# Initialize the DAO
fishDAO = FishDAO()

@app.route('/')
def index():
    return render_template('index.html')

# API to get all fish
@app.route('/api/fish', methods=['GET'])
def getAll():
    results = fishDAO.getAll()
    return jsonify(results)

# API to get a specific fish by ID
@app.route('/api/fish/<int:id>', methods=['GET'])
def findById(id):
    foundFish = fishDAO.findByID(id)
    if foundFish:
        return jsonify(foundFish)
    else:
        abort(404)

# API to create a new fish entry
@app.route('/api/fish', methods=['POST'])
def create():
    if not request.json or not 'species_name' in request.json:
        abort(400)
    fish = {
        "species_name": request.json['species_name'],
        "tank_name": request.json['tank_name'],
        "date_added": request.json['date_added'],
        "notes": request.json.get('notes', '')
    }
    addedFish = fishDAO.create(fish)
    return jsonify(addedFish), 201

# API to update an existing fish entry
@app.route('/api/fish/<int:id>', methods=['PUT'])
def update(id):
    foundFish = fishDAO.findByID(id)
    if not foundFish:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'species_name' in reqJson:
        foundFish['species_name'] = reqJson['species_name']
    if 'tank_name' in reqJson:
        foundFish['tank_name'] = reqJson['tank_name']
    if 'date_added' in reqJson:
        foundFish['date_added'] = reqJson['date_added']
    if 'notes' in reqJson:
        foundFish['notes'] = reqJson['notes']
    
    fishDAO.update(id, foundFish)
    return jsonify(foundFish)

# API to delete a fish entry
@app.route('/api/fish/<int:id>', methods=['DELETE'])
def delete(id):
    fishDAO.delete(id)
    return jsonify({"done": True})

if __name__ == '__main__':
    app.run(debug=True)