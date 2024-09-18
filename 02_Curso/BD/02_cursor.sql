-- SOLUCION --
-- Actividad 2: Uso de Cursores para Calcular Total de Ventas
-- Crear el procedimiento almacenado
CREATE PROCEDURE CalcularTotalVentas
AS
BEGIN
    -- Variables para almacenar el cálculo
    DECLARE @TotalVentas DECIMAL(18, 2)
    SET @TotalVentas = 0

    -- Declaración del cursor para recorrer los registros de ventas
    DECLARE VentasCursor CURSOR FOR
    SELECT P.Precio, RV.Cantidad
    FROM Producto P
    INNER JOIN Registro_Ventas RV ON P.ID = RV.Id_producto

    -- Variables para almacenar los valores de precio y cantidad durante la iteración del cursor
    DECLARE @Precio DECIMAL(18, 2)
    DECLARE @Cantidad INT

    -- Abrir el cursor
    OPEN VentasCursor

    -- Obtener el primer registro
    FETCH NEXT FROM VentasCursor INTO @Precio, @Cantidad

    -- Iterar mientras haya registros
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Calcular el total de ventas para este registro y sumarlo al total general
        SET @TotalVentas = @TotalVentas + (@Precio * @Cantidad)

        -- Obtener el siguiente registro
        FETCH NEXT FROM VentasCursor INTO @Precio, @Cantidad
    END

    -- Cerrar y liberar el cursor
    CLOSE VentasCursor
    DEALLOCATE VentasCursor

    -- Mostrar el resultado
    SELECT @TotalVentas AS 'Total de Ventas'
END

EXEC CalcularTotalVentas;
