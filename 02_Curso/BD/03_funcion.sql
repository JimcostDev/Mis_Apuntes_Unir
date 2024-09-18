
-- Crear la función para obtener el stock de un producto por su ID
CREATE FUNCTION dbo.obtener_stock_producto
(
    @ID_Producto INT -- Parámetro de entrada: ID del producto
)
RETURNS INT
AS
BEGIN
    DECLARE @Stock INT

    SELECT @Stock = Stock
    FROM Producto
    WHERE ID = @ID_Producto

    RETURN ISNULL(@Stock, 0)
END


-- Llamar a la función 
DECLARE @ID_Producto INT
SET @ID_Producto = 1 -- Cambiar el número por el ID del producto que desees consultar
SELECT dbo.obtener_stock_producto(@ID_Producto) AS 'Stock del Producto'
