# MuseoBDOO — Sistema de gestión de un museo con BDOO

## Descripción

Sistema informático que administra las piezas de un museo (obras, artistas,
colecciones, exposiciones, salas, préstamos y visitantes) utilizando una
Base de Datos Orientada a Objetos implementada con Python y ZODB. Los objetos
del dominio se almacenan de forma persistente y se relacionan entre sí mediante
referencias directas, sin esquemas tabulares ni SQL.

## Problema que resuelve

El museo "Centro Cultural Regional" administra su información en documentos
independientes, lo que dificulta consultar la ubicación de las piezas y saber
qué obras forman parte de determinadas exposiciones. Este sistema centraliza
toda la información en objetos persistentes y ofrece consultas directas sobre
el dominio: ubicación por sala, obras por exposición, obras prestadas,
estadísticas por artista y colección, entre otras.

## Objetivo

Diseñar e implementar una BDOO para administrar las piezas de un museo, sus
artistas, colecciones y exposiciones, utilizando objetos persistentes,
relaciones entre objetos y consultas orientadas al dominio.

## Tecnologías

- Python 3
- ZODB (Base de Datos Orientada a Objetos)
- Git (control de versiones)
- UML (diagrama de diseño)
- Visual Studio Code

## Modelo de objetos

| Clase | Identidad | Propiedades | Comportamiento |
|---|---|---|---|
| Obra | id_obra | titulo, anio, tipo, descripcion, estado | cambiar_ubicacion(), prestar(), devolver(), esta_disponible() |
| Artista | id_artista | nombre, nacionalidad, anio_nacimiento | — |
| Coleccion | id_coleccion | nombre, descripcion | — |
| Exposicion | id_exposicion | nombre, fecha_inicio, fecha_fin | agregar_obra(), retirar_obra(), esta_activa() |
| Sala | id_sala | nombre, capacidad, ubicacion | tiene_capacidad(), agregar_exposicion() |
| Prestamo | id_prestamo | fecha_prestamo, fecha_devolucion, estado | finalizar_prestamo(), esta_vigente() |
| Visitante | id_visitante | nombre, institucion, contacto | — |

**Relaciones** (referencias entre objetos persistentes):

- Obra → Artista (una obra tiene un autor)
- Obra → Coleccion (una obra pertenece a una colección)
- Obra → Sala (una obra está ubicada en una sala)
- Exposicion ↔ Obra (una exposición contiene varias obras; PersistentList)
- Sala ↔ Exposicion (una sala hospeda varias exposiciones)
- Prestamo → Obra y Prestamo → Visitante (navegación: prestamo.obra.titulo)

## Estructura del proyecto

```
MuseoBDOO/
├── modelos/            # Clases persistentes del dominio
│   ├── artista.py
│   ├── obra.py
│   ├── coleccion.py
│   ├── exposicion.py
│   ├── sala.py
│   ├── prestamo.py
│   └── visitante.py
├── persistencia/       # Apertura, guardado y cierre de ZODB
│   └── base_datos.py
├── servicios/          # CRUD y reglas de negocio
│   └── gestion_museo.py
├── consultas/          # Consultas orientadas al dominio
│   └── consultas.py
├── main.py             # Demostración completa (4 fases)
├── README.md
├── requirements.txt
└── .gitignore
```

## Instalación

```bash
git clone https://github.com/VictorSalazarSalinas/MuseoBDOO.git
cd MuseoBDOO
python -m venv venv
source venv/bin/activate        # Linux/Mac (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

El programa ejecuta cuatro fases de demostración: creación y guardado de
objetos, verificación de persistencia al reabrir la base, CRUD completo y
ejecución de las 13 consultas obligatorias.

## Funcionalidades

- Registro de artistas, obras, colecciones, salas, exposiciones, visitantes y préstamos (Create)
- Búsqueda por identidad y listados (Read)
- Modificación de propiedades (Update)
- Eliminación de objetos (Delete)
- Comportamientos de dominio: prestar/devolver obra, agregar/retirar obra de exposición, validar capacidad de sala
- Exportación implícita de información mediante consultas de reporte

## Consultas implementadas

1. Listar todas las obras — `listar_obras()`
2. Buscar una obra por su identidad — `buscar_obra_por_id(id)`
3. Listar obras de un artista — `listar_obras_de_artista(id)`
4. Listar obras de una colección — `listar_obras_de_coleccion(id)`
5. Mostrar obras disponibles — `listar_obras_disponibles()` (usa `esta_disponible()`)
6. Mostrar obras prestadas — `listar_obras_prestadas()`
7. Mostrar obras de una exposición — `listar_obras_de_exposicion(id)`
8. Mostrar exposiciones activas — `listar_exposiciones_activas(fecha)` (usa `esta_activa()`)
9. Mostrar obras de una sala — `listar_obras_en_sala(id)`
10. Artistas con mayor número de obras — `artistas_con_mas_obras()` (estadística)
11. Contabilizar obras por colección — `contar_obras_por_coleccion()` (estadística)
12. Obras sin exposición asignada — `listar_obras_sin_exposicion()`
13. Consulta compleja del equipo — `reporte_gestion_prestamos()`: por sala cuenta
    obras y prestadas, y calcula la antigüedad promedio de las obras
    (combina relaciones, comportamiento y estadística)

## Reglas de negocio

- No pueden registrarse dos objetos con el mismo identificador.
- Una obra solo puede prestarse si su estado es "Disponible" (`prestar()` devuelve False en caso contrario).
- Al agregar una obra a una exposición, su estado cambia a "En Exposición".
- Al retirar una obra de una exposición, regresa a estado "Disponible".
- Una sala solo acepta exposiciones si tiene capacidad disponible (`tiene_capacidad()`).
- Al crear un préstamo, la obra asociada se marca como "Prestada"; al finalizarlo se devuelve.

## Uso de Git

El proyecto se desarrolló con una rama por integrante:

```
main
├── desarrollo-integrante-1  (modelos: Coleccion, Sala, Exposicion + comportamiento)
├── desarrollo-integrante-2  (persistencia ZODB y CRUD completo)
├── desarrollo-integrante-3  (consultas orientadas al dominio)
└── desarrollo-integrante-4  (préstamos, visitantes e integración final)
```

Cada integrante configuró su identidad en Git, realizó commits funcionales
asociados a su nombre y participó en la integración mediante merge. El
historial (`git log --oneline`) permite identificar qué hizo cada integrante.

## Integrantes

- VictorSalazarSalinas
- Jmnsitxo
- Mahyli
- victor

## Autores

Equipo de Bases de Datos Avanzadas — Universidad de Xalapa, septiembre de 2026.
