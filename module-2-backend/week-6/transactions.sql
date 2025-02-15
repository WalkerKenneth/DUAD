-- Create the database
CREATE DATABASE Store;
USE Store;

-- Create the User table
CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create the Products table
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0)
);

-- Create the Bill table
CREATE TABLE Bill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    bill_status ENUM('completed', 'revoked') DEFAULT 'completed',
    FOREIGN KEY (user_id) REFERENCES User(id)
);

-- Create the Bill_Products table
CREATE TABLE Bill_Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (bill_id) REFERENCES Bill(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

-- Buy Product 
DELIMITER $$
CREATE PROCEDURE Buy_Product(
    IN p_user_id INT, 
    IN p_product_id INT, 
    IN p_quantity INT
)
BEGIN
    DECLARE v_price DECIMAL(10,2);
    DECLARE v_stock INT;
    DECLARE v_total DECIMAL(10,2);
    DECLARE v_bill_id INT;
    
    START TRANSACTION;
    
    -- Validate if the product has enough stock
    SELECT stock, precio INTO v_stock, v_precio FROM Productos WHERE id = p_producto_id;
    IF v_stock < p_cantidad THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stock insuficiente';
    END IF;
    
    -- Validate if the user exists
    IF NOT EXISTS (SELECT 1 FROM Usuarios WHERE id = p_usuario_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Usuario no encontrado';
    END IF;
    
    -- Create the bill
    SET v_total = v_price * p_quantity;
    INSERT INTO Bill (user_id, total) VALUES (p_user_id, v_total);
    SET v_bill_id = LAST_INSERT_ID();
    
    -- Add products to the bill
    INSERT INTO Bill_Products (bill_id, product_id, quantity, subtotal) 
    VALUES (v_bill_id, p_product_id, p_quantity, v_total);
    
    -- Reduce the stock of the product
    UPDATE Products SET stock = stock - p_quantity WHERE id = p_product_id;
    
    COMMIT;
END $$
DELIMITER ;

-- Return Product
DELIMITER $$
CREATE PROCEDURE Return_Product(
    IN p_bill_id INT
)
BEGIN
    DECLARE v_exist INT;
    
    START TRANSACTION;
    
    -- Validate if the bill exists and is not returned
    SELECT COUNT(*) INTO v_exist FROM Bill WHERE id = p_bill_id AND bill_status = 'completed';
    IF v_exist = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Bill not found or already returned';
    END IF;
    
    -- Increase the stock of the purchased products
    UPDATE Products p
    JOIN Bill_Products bp ON p.id = bp.product_id
    SET p.stock = p.stock + bp.quantity
    WHERE bp.bill_id = p_bill_id;
    
    -- Mark the bill as returned
    UPDATE Bill SET bill_status = 'revoked' WHERE id = p_bill_id;
    
    COMMIT;
END $$
DELIMITER ;
