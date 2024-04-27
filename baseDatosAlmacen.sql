Create Table registroAlmacen(
	Codigo varchar (255) ,
	Producto varchar (255) ,
	Proveedor varchar (255) ,
	Descripcion varchar (255) ,
	Stock varchar (255) ,
	PrecioUnitario varchar (255) ,
	FechaProduccion varchar (255) ,
	FechaVencimiento varchar (255) ,
	
);
INSERT INTO registroAlmacen (Codigo, Producto, Proveedor, Descripcion, Stock, PrecioUnitario, FechaProduccion, FechaVencimiento)
VALUES
  ('p001', 'Galleta', 'mymaskot', 'Galleta para perro cachorro', '12', '5', '12-09-2021', '23-07-2022');

  SELECT * FROM registroAlmacen;