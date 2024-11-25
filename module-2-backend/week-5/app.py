from flask import Flask, request, jsonify
from database import execute_query, get_db_connection

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    query = """
    INSERT INTO lyfter_car_rental.users (name, email, username, hashed_password, date_of_birth, account_status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (
        data['name'],
        data['email'],
        data['username'],
        data['hashed_password'],
        data['date_of_birth'],
        data.get('account_status', 'active')
    )
    execute_query(query, params)
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    query = """
    INSERT INTO lyfter_car_rental.cars (brand, model, year_of_manufacture, car_status)
    VALUES (%s, %s, %s, %s)
    """
    params = (
        data['brand'],
        data['model'],
        data['year_of_manufacture'],
        data.get('car_status', 'available')
    )
    execute_query(query, params)
    return jsonify({'message': 'Car created successfully'}), 201

@app.route('/rentals', methods=['POST'])
def create_rental():
    data = request.json
    query = """
    INSERT INTO lyfter_car_rental.rentals (user_id, car_id)
    VALUES (%s, %s)
    """
    params = (data['user_id'], data['car_id'])
    execute_query(query, params)
    return jsonify({'message': 'Rental created successfully'}), 201

@app.route('/cars/<int:car_id>/status', methods=['PUT'])
def update_car_status(car_id):
    data = request.json
    query = "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE id = %s"
    params = (data['car_status'], car_id)
    execute_query(query, params)
    return jsonify({'message': 'Car status updated successfully'})

@app.route('/users/<int:user_id>/status', methods=['PUT'])
def update_user_status(user_id):
    data = request.json
    query = "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s"
    params = (data['account_status'], user_id)
    execute_query(query, params)
    return jsonify({'message': 'User status updated successfully'})

@app.route('/rentals/<int:rental_id>/complete', methods=['PUT'])
def complete_rental(rental_id):
    query_rental = "UPDATE lyfter_car_rental.rentals SET rental_status = 'completed' WHERE id = %s"
    query_car = """
    UPDATE lyfter_car_rental.cars
    SET car_status = 'available'
    WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)
    """
    execute_query(query_rental, (rental_id,))
    execute_query(query_car, (rental_id,))
    return jsonify({'message': 'Rental completed successfully'})

@app.route('/rentals', methods=['GET'])
def list_rentals():
    status = request.args.get('status')
    query = "SELECT * FROM lyfter_car_rental.rentals"
    if status:
        query += " WHERE rental_status = %s"
        params = (status,)
    else:
        params = None
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rentals = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rentals)
