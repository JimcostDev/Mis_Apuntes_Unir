-- Crear el procedimiento para actualizar el stock de un producto
CREATE PROCEDURE actualizar_stock
    @ID_Producto INT,
    @CantidadVendida INT
AS
BEGIN
    DECLARE @StockActual INT

    -- Obtener el stock actual del producto
    SELECT @StockActual = Stock
    FROM Producto
    WHERE ID = @ID_Producto

    -- Actualizar el stock restando la cantidad vendida
    UPDATE Producto
    SET Stock = @StockActual - @CantidadVendida
    WHERE ID = @ID_Producto
END

-- usar sp
DECLARE @ID_ProductoVenta INT
DECLARE @CantidadVenta INT

SET @ID_ProductoVenta = 1 -- Cambiar por el ID del producto vendido
SET @CantidadVenta = 5 -- Cambiar por la cantidad vendida
SELECT * FROM Producto WHERE ID = @ID_ProductoVenta -- ver cantidad actal

EXEC actualizar_stock @ID_Producto = @ID_ProductoVenta, @CantidadVendida = @CantidadVenta;
SELECT * FROM Producto WHERE ID = @ID_ProductoVenta -- ver cantidad despues del update