CREATE DATABASE Store;
USE Store;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0)
);

CREATE TABLE Bill (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    bill_status ENUM('completada', 'retornada') DEFAULT 'completada',
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Factura_Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    factura_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (factura_id) REFERENCES Facturas(id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id)
);

-- 2. Transacción para realizar una compra
DELIMITER $$
CREATE PROCEDURE RealizarCompra(
    IN p_usuario_id INT, 
    IN p_producto_id INT, 
    IN p_cantidad INT
)
BEGIN
    DECLARE v_precio DECIMAL(10,2);
    DECLARE v_stock INT;
    DECLARE v_total DECIMAL(10,2);
    DECLARE v_factura_id INT;
    
    START TRANSACTION;
    
    -- Validar que el producto tiene suficiente stock
    SELECT stock, precio INTO v_stock, v_precio FROM Productos WHERE id = p_producto_id;
    IF v_stock < p_cantidad THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stock insuficiente';
    END IF;
    
    -- Validar que el usuario existe
    IF NOT EXISTS (SELECT 1 FROM Usuarios WHERE id = p_usuario_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Usuario no encontrado';
    END IF;
    
    -- Crear la factura
    SET v_total = v_precio * p_cantidad;
    INSERT INTO Facturas (usuario_id, total) VALUES (p_usuario_id, v_total);
    SET v_factura_id = LAST_INSERT_ID();
    
    -- Agregar productos a la factura
    INSERT INTO Factura_Productos (factura_id, producto_id, cantidad, subtotal) 
    VALUES (v_factura_id, p_producto_id, p_cantidad, v_total);
    
    -- Reducir el stock del producto
    UPDATE Productos SET stock = stock - p_cantidad WHERE id = p_producto_id;
    
    COMMIT;
END $$
DELIMITER ;

-- 3. Transacción para el retorno de un producto
DELIMITER $$
CREATE PROCEDURE RetornarProducto(
    IN p_factura_id INT
)
BEGIN
    DECLARE v_exist INT;
    
    START TRANSACTION;
    
    -- Validar que la factura existe y no ha sido retornada
    SELECT COUNT(*) INTO v_exist FROM Facturas WHERE id = p_factura_id AND estado = 'completada';
    IF v_exist = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Factura no encontrada o ya retornada';
    END IF;
    
    -- Aumentar el stock de los productos comprados
    UPDATE Productos p
    JOIN Factura_Productos fp ON p.id = fp.producto_id
    SET p.stock = p.stock + fp.cantidad
    WHERE fp.factura_id = p_factura_id;
    
    -- Marcar la factura como retornada
    UPDATE Facturas SET estado = 'retornada' WHERE id = p_factura_id;
    
    COMMIT;
END $$
DELIMITER ;
