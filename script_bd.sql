CREATE DATABASE autos_colombia;
USE autos_colombia;

CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    hora_entrada DATETIME NOT NULL,
    hora_salida DATETIME NULL,
    estado VARCHAR(15) DEFAULT 'Adentro'
);