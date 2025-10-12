--proyecto grupal 

--Crear tablas 
DROP TABLE IF EXISTS evaluacion;
DROP TABLE IF EXISTS alumnos;
DROP TABLE IF EXISTS profesor;
DROP TABLE IF EXISTS proyecto;
DROP TABLE IF EXISTS curso;
DROP TABLE IF EXISTS vertical;
DROP TABLE IF EXISTS escuela;

CREATE TABLE IF NOT EXISTS escuela (
    id_campus serial NOT NULL,
    campus text,
    PRIMARY KEY (id_campus)
);

CREATE TABLE IF NOT EXISTS vertical (
    id_ver serial NOT NULL,
    vertical text,
    PRIMARY KEY (id_ver)
);

CREATE TABLE IF NOT EXISTS curso (
    id_curso serial NOT NULL,
    promocion text,
    fecha date,
    id_campus smallint,
    PRIMARY KEY (id_curso),
    FOREIGN KEY (id_campus) REFERENCES escuela(id_campus) 
);

CREATE TABLE IF NOT EXISTS alumnos (
    id_alumnos serial NOT NULL,
    nombre text,
    correo text,
    id_curso smallint,
    PRIMARY KEY (id_alumnos),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso) 
);

CREATE TABLE IF NOT EXISTS proyecto (
    id_proyecto serial NOT NULL,
    nombre_proyecto text,
    id_vertical smallint,
    PRIMARY KEY (id_proyecto),
    FOREIGN KEY (id_vertical) REFERENCES vertical(id_ver)        
);

CREATE TABLE IF NOT EXISTS evaluacion (
    id_evaluacion serial NOT NULL,
    id_alumno smallint NOT NULL,
    id_proyecto smallint NOT NULL ,
    nota text,
    PRIMARY KEY (id_evaluacion),
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumnos),
    FOREIGN KEY (id_proyecto) REFERENCES proyecto (id_proyecto)
);

CREATE TABLE IF NOT EXISTS profesor (
    id_profesor serial NOT NULL,
    nombre text,
    rol text,
    id_curso smallint,
    id_vertical smallint,
    modalidad text,
    PRIMARY KEY (id_profesor),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (id_vertical) REFERENCES vertical(id_ver)  
);


--Insertar informacion a las tablas 

INSERT INTO escuela (id_campus, campus) VALUES 
(1, 'Madrid'),
(0, 'Valencia');

INSERT INTO vertical (id_ver, vertical) VALUES
(0, 'DS'),
(1, 'FS');

INSERT INTO curso (id_curso, promocion, fecha, id_campus) VALUES 
(0, 'Septiembre', '2023-09-18', 1),
(1, 'Febrero', '2024-02-12', 1),
(2, 'Febrero', '2024-02-12', 0),
(3, 'Septiembre', '2023-09-18', 0);

INSERT INTO proyecto (id_proyecto, nombre_proyecto, id_vertical) VALUES 
(0, 'Proyecto_HLF', 0),
(1, 'Proyecto_EDA', 0),
(2, 'Proyecto_BBDD', 0),
(3, 'Proyecto_ML', 0),
(4, 'Proyecto_Deployment', 0),
(5, 'Proyecto_React', 1),
(6, 'Proyecto_Backend', 1),
(7, 'Proyecto_FrontEnd', 1),
(8, 'Proyecto_WebDev', 1),
(9, 'Proyecto_FullSatck', 1);

INSERT INTO profesores (id_profesor, nombre, rol, id_curso, modalidad, id_vertical) VALUES
(0, 'Noa Yáñez', 'TA', 0, 'Presencial', 0),
(1, 'Saturnina Benitez', 'TA', 0, 'Presencial', 0),
(2, 'Anna Feliu', 'TA', 0, 'Presencial', 1),
(3, 'Rosalva Ayuso', 'TA', 3, 'Presencial', 1),
(4, 'Ana Sofía Ferrer', 'TA', 2, 'Presencial', 1),
(5, 'Angélica Corral', 'TA', 1, 'Presencial', 1),
(6, 'Ariel Lledó', 'TA', 0, 'Presencial', 0),
(7, 'Mario Prats', 'LI', 2, 'Online', 1),
(8, 'Luis Ángel Suárez', 'LI', 0, 'Online', 1),
(9, 'María Dolores Diaz', 'LI', 0, 'Online', 0);

INSERT INTO alumnos (id_alumnos, nombre, correo, id_curso) VALUES
(23, 'Isabel Ibáñez', 'Isabel_Ibáñez@gmail.com', 1),
(24, 'Desiderio Jordá', 'Desiderio_Jordá@gmail.com', 1),
(25, 'Rosalina Llanos', 'Rosalina_Llanos@gmail.com', 1),
(26, 'Amor Larrañaga', 'Amor_Larrañaga@gmail.com', 0),
(27, 'Teodoro Alberola', 'Teodoro_Alberola@gmail.com', 0),
(28, 'Cleto Plana', 'Cleto_Plana@gmail.com', 0),
(29, 'Aitana Sebastián', 'Aitana_Sebastián@gmail.com', 0),
(30, 'Dolores Valbuena', 'Dolores_Valbuena@gmail.com', 0),
(31, 'Julie Ferrer', 'Julie_Ferrer@gmail.com', 0),
(32, 'Mireia Cabañas', 'Mireia_Cabañas@gmail.com', 0),
(33, 'Flavia Amador', 'Flavia_Amador@gmail.com', 0),
(34, 'Albino Macias', 'Albino_Macias@gmail.com', 0),
(35, 'Ester Sánchez', 'Ester_Sánchez@gmail.com', 0),
(0, 'Jafet Casals', 'Jafet_Casals@gmail.com', 0),
(1, 'Jorge Manzanares', 'Jorge_Manzanares@gmail.com', 0),
(2, 'Onofre Adadia', 'Onofre_Adadia@gmail.com', 0),
(3, 'Merche Prada', 'Merche_Prada@gmail.com', 0),
(4, 'Pilar Abella', 'Pilar_Abella@gmail.com', 0),
(5, 'Leoncio Tena', 'Leoncio_Tena@gmail.com', 0),
(6, 'Odalys Torrijos', 'Odalys_Torrijos@gmail.com', 0),
(7, 'Eduardo Caparrós', 'Eduardo_Caparrós@gmail.com', 0),
(8, 'Ignacio Goicoechea', 'Ignacio_Goicoechea@gmail.com', 0),
(9, 'Clementina Santos', 'Clementina_Santos@gmail.com', 0),
(10, 'Daniela Falcó', 'Daniela_Falcó@gmail.com', 0),
(11, 'Abraham Vélez', 'Abraham_Vélez@gmail.com', 0),
(12, 'Maximiliano Menéndez', 'Maximiliano_Menéndez@gmail.com', 0),
(13, 'Anita Heredia', 'Anita_Heredia@gmail.com', 0),
(15, 'Eli Casas', 'Eli_Casas@gmail.com', 0),
(16, 'Guillermo Borrego', 'Guillermo_Borrego@gmail.com', 1),
(17, 'Sergio Aguirre', 'Sergio_Aguirre@gmail.com', 1),
(18, 'Carlito Carrión', 'Carlito_Carrión@gmail.com', 1),
(19, 'Haydée Figueroa', 'Haydée_Figueroa@gmail.com', 1),
(20, 'Chita Mancebo', 'Chita_Mancebo@gmail.com', 1),
(21, 'Joaquina Asensio', 'Joaquina_Asensio@gmail.com', 1),
(22, 'Cristian Sarabia', 'Cristian_Sarabia@gmail.com', 1),
(36, 'Luis Miguel Galvez', 'Luis_Miguel_Galvez@gmail.com', 0),
(37, 'Loida Arellano', 'Loida_Arellano@gmail.com', 0),
(38, 'Heraclio Duque', 'Heraclio_Duque@gmail.com', 0),
(39, 'Herberto Figueras', 'Herberto_Figueras@gmail.com', 0),
(40, 'Teresa Laguna', 'Teresa_Laguna@gmail.com', 2),
(41, 'Estrella Murillo', 'Estrella_Murillo@gmail.com', 2),
(42, 'Ernesto Uriarte', 'Ernesto_Uriarte@gmail.com', 2),
(43, 'Daniela Guitart', 'Daniela_Guitart@gmail.com', 2),
(44, 'Timoteo Trillo', 'Timoteo_Trillo@gmail.com', 2),
(45, 'Ricarda Tovar', 'Ricarda_Tovar@gmail.com', 2),
(46, 'Alejandra Vilaplana', 'Alejandra_Vilaplana@gmail.com', 2),
(47, 'Daniel Rosselló', 'Daniel_Rosselló@gmail.com', 2),
(48, 'Rita Olivares', 'Rita_Olivares@gmail.com', 2),
(49, 'Cleto Montes', 'Cleto_Montes@gmail.com', 2),
(50, 'Marino Castilla', 'Marino_Castilla@gmail.com', 2),
(51, 'Estefanía Valcárcel', 'Estefanía_Valcárcel@gmail.com', 2),
(52, 'Noemí Vilanova', 'Noemí_Vilanova@gmail.com', 2);

INSERT INTO evaluacion VALUES
(0, 0, 0, 'Apto'),
(1, 1, 0, 'Apto'),
(2, 2, 0, 'Apto'),
(3, 3, 0, 'Apto'),
(4, 4, 0, 'Apto'),
(5, 5, 0, 'Apto'),
(6, 6, 0, 'No Apto'),
(7, 7, 0, 'No Apto'),
(8, 8, 0, 'Apto'),
(9, 9, 0, 'Apto'),
(10, 10, 0, 'Apto'),
(11, 11, 0, 'Apto'),
(12, 12, 0, 'Apto'),
(13, 13, 0, 'Apto'),
(14, 15, 0, 'Apto'),
(15, 0, 1, 'No Apto'),
(16, 1, 1, 'No Apto'),
(17, 2, 1, 'Apto'),
(18, 3, 1, 'No Apto'),
(19, 4, 1, 'No Apto'),
(20, 5, 1, 'Apto'),
(21, 6, 1, 'Apto'),
(22, 7, 1, 'Apto'),
(23, 8, 1, 'Apto'),
(24, 9, 1, 'No Apto'),
(25, 10, 1, 'Apto'),
(26, 11, 1, 'No Apto'),
(27, 12, 1, 'No Apto'),
(28, 13, 1, 'Apto'),
(29, 15, 1, 'Apto'),
(30, 0, 2, 'Apto'),
(31, 1, 2, 'Apto'),
(32, 2, 2, 'Apto'),
(33, 3, 2, 'No Apto'),
(34, 4, 2, 'Apto'),
(35, 5, 2, 'Apto'),
(36, 6, 2, 'Apto'),
(37, 7, 2, 'Apto'),
(38, 8, 2, 'Apto'),
(39, 9, 2, 'Apto'),
(40, 10, 2, 'Apto'),
(41, 11, 2, 'No Apto'),
(42, 12, 2, 'Apto'),
(43, 13, 2, 'Apto'),
(44, 15, 2, 'Apto'),
(45, 0, 3, 'Apto'),
(46, 1, 3, 'Apto'),
(47, 2, 3, 'No Apto'),
(48, 3, 3, 'Apto'),
(49, 4, 3, 'Apto'),
(50, 5, 3, 'Apto'),
(51, 6, 3, 'Apto'),
(52, 7, 3, 'Apto'),
(53, 8, 3, 'No Apto'),
(54, 9, 3, 'Apto'),
(55, 10, 3, 'Apto'),
(56, 11, 3, 'Apto'),
(57, 12, 3, 'Apto'),
(58, 13, 3, 'Apto'),
(59, 15, 3, 'Apto'),
(60, 0, 4, 'Apto'),
(61, 1, 4, 'Apto'),
(62, 2, 4, 'Apto'),
(63, 3, 4, 'No Apto'),
(64, 4, 4, 'Apto'),
(65, 5, 4, 'Apto'),
(66, 6, 4, 'Apto'),
(67, 7, 4, 'Apto'),
(68, 8, 4, 'Apto'),
(69, 9, 4, 'Apto'),
(70, 10, 4, 'Apto'),
(71, 11, 4, 'Apto'),
(72, 12, 4, 'Apto'),
(73, 13, 4, 'Apto'),
(74, 15, 4, 'Apto'),
(75, 16, 0, 'Apto'),
(76, 17, 0, 'Apto'),
(77, 18, 0, 'Apto'),
(78, 19, 0, 'Apto'),
(79, 20, 0, 'No Apto'),
(80, 21, 0, 'No Apto'),
(81, 22, 0, 'Apto'),
(82, 23, 0, 'No Apto'),
(83, 24, 0, 'No Apto'),
(84, 25, 0, 'Apto'),
(85, 16, 1, 'No Apto'),
(86, 17, 1, 'No Apto'),
(87, 18, 1, 'No Apto'),
(88, 19, 1, 'Apto'),
(89, 20, 1, 'Apto'),
(90, 21, 1, 'No Apto'),
(91, 22, 1, 'Apto'),
(92, 23, 1, 'Apto'),
(93, 24, 1, 'Apto'),
(94, 25, 1, 'Apto'),
(95, 16, 2, 'No Apto'),
(96, 17, 2, 'Apto'),
(97, 18, 2, 'Apto'),
(98, 19, 2, 'Apto'),
(99, 20, 2, 'No Apto'),
(100, 21, 2, 'Apto'),
(101, 22, 2, 'No Apto'),
(102, 23, 2, 'No Apto'),
(103, 24, 2, 'No Apto'),
(104, 25, 2, 'Apto'),
(105, 16, 3, 'Apto'),
(106, 17, 3, 'Apto'),
(107, 18, 3, 'Apto'),
(108, 19, 3, 'Apto'),
(109, 20, 3, 'Apto'),
(110, 21, 3, 'Apto'),
(111, 22, 3, 'Apto'),
(112, 23, 3, 'Apto'),
(113, 24, 3, 'No Apto'),
(114, 25, 3, 'Apto'),
(115, 16, 4, 'No Apto'),
(116, 17, 4, 'No Apto'),
(117, 18, 4, 'Apto'),
(118, 19, 4, 'Apto'),
(119, 20, 4, 'Apto'),
(120, 21, 4, 'Apto'),
(121, 22, 4, 'Apto'),
(122, 23, 4, 'Apto'),
(123, 24, 4, 'Apto'),
(124, 25, 4, 'Apto'),
(125, 26, 8, 'Apto'),
(126, 27, 8, 'No Apto'),
(127, 28, 8, 'Apto'),
(128, 29, 8, 'Apto'),
(129, 30, 8, 'Apto'),
(130, 31, 8, 'No Apto'),
(131, 32, 8, 'No Apto'),
(132, 33, 8, 'Apto'),
(133, 34, 8, 'No Apto'),
(134, 35, 8, 'No Apto'),
(135, 36, 8, 'No Apto'),
(136, 37, 8, 'Apto'),
(137, 38, 8, 'Apto'),
(138, 39, 8, 'Apto'),
(139, 26, 7, 'Apto'),
(140, 27, 7, 'No Apto'),
(141, 28, 7, 'No Apto'),
(142, 29, 7, 'No Apto'),
(143, 30, 7, 'Apto'),
(144, 31, 7, 'No Apto'),
(145, 32, 7, 'Apto'),
(146, 33, 7, 'Apto'),
(147, 34, 7, 'Apto'),
(148, 35, 7, 'Apto'),
(149, 36, 7, 'Apto'),
(150, 37, 7, 'Apto'),
(151, 38, 7, 'Apto'),
(152, 39, 7, 'Apto'),
(153, 26, 6, 'Apto'),
(154, 27, 6, 'Apto'),
(155, 28, 6, 'Apto'),
(156, 29, 6, 'Apto'),
(157, 30, 6, 'Apto'),
(158, 31, 6, 'No Apto'),
(159, 32, 6, 'Apto'),
(160, 33, 6, 'No Apto'),
(161, 34, 6, 'Apto'),
(162, 35, 6, 'Apto'),
(163, 36, 6, 'Apto'),
(164, 37, 6, 'Apto'),
(165, 38, 6, 'No Apto'),
(166, 39, 6, 'Apto'),
(167, 26, 5, 'Apto'),
(168, 27, 5, 'No Apto'),
(169, 28, 5, 'No Apto'),
(170, 29, 5, 'No Apto'),
(171, 30, 5, 'Apto'),
(172, 31, 5, 'Apto'),
(173, 32, 5, 'Apto'),
(174, 33, 5, 'Apto'),
(175, 34, 5, 'Apto'),
(176, 35, 5, 'No Apto'),
(177, 36, 5, 'Apto'),
(178, 37, 5, 'Apto'),
(179, 38, 5, 'No Apto'),
(180, 39, 5, 'Apto'),
(181, 26, 9, 'No Apto'),
(182, 27, 9, 'Apto'),
(183, 28, 9, 'Apto'),
(184, 29, 9, 'Apto'),
(185, 30, 9, 'No Apto'),
(186, 31, 9, 'No Apto'),
(187, 32, 9, 'Apto'),
(188, 33, 9, 'Apto'),
(189, 34, 9, 'Apto'),
(190, 35, 9, 'Apto'),
(191, 36, 9, 'Apto'),
(192, 37, 9, 'Apto'),
(193, 38, 9, 'No Apto'),
(194, 39, 9, 'Apto'),
(195, 40, 8, 'Apto'),
(196, 41, 8, 'Apto'),
(197, 42, 8, 'Apto'),
(198, 43, 8, 'Apto'),
(199, 44, 8, 'No Apto'),
(200, 45, 8, 'Apto'),
(201, 46, 8, 'No Apto'),
(202, 47, 8, 'No Apto'),
(203, 48, 8, 'No Apto'),
(204, 49, 8, 'Apto'),
(205, 50, 8, 'No Apto'),
(206, 51, 8, 'Apto'),
(207, 52, 8, 'Apto'),
(208, 40, 7, 'Apto'),
(209, 41, 7, 'Apto'),
(210, 42, 7, 'Apto'),
(211, 43, 7, 'No Apto'),
(212, 44, 7, 'Apto'),
(213, 45, 7, 'Apto'),
(214, 46, 7, 'No Apto'),
(215, 47, 7, 'No Apto'),
(216, 48, 7, 'No Apto'),
(217, 49, 7, 'Apto'),
(218, 50, 7, 'No Apto'),
(219, 51, 7, 'Apto'),
(220, 52, 7, 'No Apto'),
(221, 40, 6, 'Apto'),
(222, 41, 6, 'No Apto'),
(223, 42, 6, 'Apto'),
(224, 43, 6, 'No Apto'),
(225, 44, 6, 'Apto'),
(226, 45, 6, 'Apto'),
(227, 46, 6, 'No Apto'),
(228, 47, 6, 'Apto'),
(229, 48, 6, 'No Apto'),
(230, 49, 6, 'No Apto'),
(231, 50, 6, 'Apto'),
(232, 51, 6, 'No Apto'),
(233, 52, 6, 'No Apto'),
(234, 40, 5, 'Apto'),
(235, 41, 5, 'Apto'),
(236, 42, 5, 'Apto'),
(237, 43, 5, 'Apto'),
(238, 44, 5, 'Apto'),
(239, 45, 5, 'Apto'),
(240, 46, 5, 'Apto'),
(241, 47, 5, 'No Apto'),
(242, 48, 5, 'Apto'),
(243, 49, 5, 'Apto'),
(244, 50, 5, 'No Apto'),
(245, 51, 5, 'No Apto'),
(246, 52, 5, 'Apto'),
(247, 40, 9, 'Apto'),
(248, 41, 9, 'Apto'),
(249, 42, 9, 'Apto'),
(250, 43, 9, 'Apto'),
(251, 44, 9, 'No Apto'),
(252, 45, 9, 'Apto'),
(253, 46, 9, 'Apto'),
(254, 47, 9, 'No Apto'),
(255, 48, 9, 'Apto'),
(256, 49, 9, 'Apto'),
(257, 50, 9, 'No Apto'),
(258, 51, 9, 'Apto'),
(259, 52, 9, 'Apto');

--Querys
-- Obtener las notas de todos los alumnos de la promoción de febrero en Madrid
SELECT a.nombre, c.promocion, e.nota, p.nombre_proyecto
FROM alumnos a
JOIN curso c ON a.id_curso = c.id_curso
JOIN evaluacion e ON a.id_alumnos = e.id_alumno
JOIN proyecto p ON e.id_proyecto = p.id_proyecto
JOIN escuela esc ON c.id_campus = esc.id_campus
WHERE c.promocion = 'Febrero' AND esc.campus = 'Madrid';

-- Alumnos que no han superado algún proyecto
SELECT DISTINCT
    a.nombre,
    a.correo,
	p.nombre_proyecto
FROM evaluacion AS e
JOIN alumnos AS a
    ON e.id_alumno = a.id_alumnos
JOIN proyecto AS p
	ON e.id_proyecto = p.id_proyecto
WHERE e.nota = 'No Apto';

SELECT a."ID_Alumnos",
a."Nombre",
a."Correo",
c."Promocion",
c."Fecha",
e."Campus",
l."Nota",
y."Nombre_proyecto"
FROM "Alumnos" as a
JOIN "Curso" as c
ON a."ID_Curso" = c."ID_Curso"
JOIN "Escuela" as e
ON c."ID_Campus" = e."ID_Campus"
JOIN "Evaluacion" as l
ON a."ID_Alumnos" = l."ID_Alumno"
JOIN "Proyecto" as y
ON l."ID_Proyecto" = y."ID_Proyecto"