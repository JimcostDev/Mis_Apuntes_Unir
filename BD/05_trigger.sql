--  (trigger) para actualizar el stock después de insertar en Registro_Ventas
CREATE TRIGGER trg_actualizar_stock
ON Registro_Ventas
INSTEAD OF INSERT
AS
BEGIN
    DECLARE @ID_Producto INT, @CantidadVendida INT

    -- Obtener el ID del producto y la cantidad vendida de la fila insertada
    SELECT @ID_Producto = Id_producto, @CantidadVendida = Cantidad
    FROM inserted

    -- Actualizar el stock restando la cantidad vendida
    IF EXISTS (SELECT 1 FROM Producto WHERE ID = @ID_Producto)
    BEGIN
        UPDATE Producto
        SET Stock = Stock - @CantidadVendida
        WHERE ID = @ID_Producto
    END
    ELSE
    BEGIN
        -- Si el producto no existe, generar un mensaje de error
        RAISERROR ('El producto no existe.', 16, 1)
        ROLLBACK TRANSACTION
    END
END

-- probrar
INSERT INTO Registro_Ventas (Id_producto, Cantidad, Fecha_Venta)
VALUES (1, 5, GETDATE()) 

SELECT * FROM Producto WHERE ID = 1 

-- probar con producto no existente
INSERT INTO Registro_Ventas (Id_producto, Cantidad, Fecha_Venta)
VALUES (1000, 10, GETDATE()) -- Suponiendo que no existe un producto con ID 1000
