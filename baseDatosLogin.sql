Create Table registroLogin(
correo varchar (255) ,
nombre varchar (255) ,
apellido varchar (255) ,
contraseņa varchar (255) ,
celular varchar (255) ,
nacimiento varchar (255) ,
permisos varchar (255) ,
genero varchar (255) ,
);
INSERT INTO registroLogin (correo,nombre,apellido,contraseņa,celular,nacimiento,permisos,genero)
VALUES
  ('carlos@animalia.com','carlos','acosta','1234','987654654','04-08-2001','Administrador','Masculino');

SELECT * FROM registroLogin
  

