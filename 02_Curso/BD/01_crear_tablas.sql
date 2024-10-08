-- SOLUCION --
-- Actividad 1: Creación de Tablas y Carga de Datos

USE [Test]
GO
/****** Object:  Table [dbo].[Producto]    Script Date: 28/11/2023 10:33:20 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Producto](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Nombre] [varchar](50) NULL,
	[Precio] [float] NULL,
	[Stock] [int] NULL,
 CONSTRAINT [PK_Producto] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Registro_Ventas]    Script Date: 28/11/2023 10:33:20 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Registro_Ventas](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Id_Producto] [int] NULL,
	[Cantidad] [int] NULL,
	[Fecha_Venta] [date] NULL,
 CONSTRAINT [PK_Registro_Ventas] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Registro_Ventas]  WITH CHECK ADD  CONSTRAINT [FK_Registro_Ventas_Producto] FOREIGN KEY([Id_Producto])
REFERENCES [dbo].[Producto] ([ID])
GO
ALTER TABLE [dbo].[Registro_Ventas] CHECK CONSTRAINT [FK_Registro_Ventas_Producto]
GO
