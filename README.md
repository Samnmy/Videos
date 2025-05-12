# Video Library Management

Este proyecto tiene como objetivo gestionar una biblioteca de videos o películas, permitiendo realizar diversas operaciones como registrar, buscar, actualizar, eliminar y generar informes sobre las películas disponibles en la biblioteca.

## Funcionalidades

El código implementa las siguientes funcionalidades clave:

1. **Registrar una película**: Permite agregar nuevas películas a la biblioteca con detalles como el título, director, género, año de estreno, cantidad disponible y precio de alquiler.
   
2. **Buscar una película**: Permite buscar películas por título o director. La búsqueda es insensible a mayúsculas/minúsculas.
   
3. **Actualizar información de una película**: Se puede actualizar la cantidad de copias disponibles o el precio de alquiler de una película existente.
   
4. **Eliminar una película**: Permite eliminar una película de la biblioteca después de confirmar la acción.
   
5. **Generar informes**: Calcula el valor total de inventario de las películas y genera un informe por género con la película más antigua y más reciente.

6. **Menú interactivo**: Ofrece una interfaz de usuario basada en texto para interactuar con el sistema de gestión de la biblioteca de videos.

## Cómo funciona

El sistema mantiene una lista de diccionarios (`video_library`), donde cada diccionario contiene la información de una película. Se definen varias funciones que permiten modificar esta lista o interactuar con los datos:

- **register_movie**: Registra una nueva película en la biblioteca tras validar los datos de entrada (como año, cantidad y precio).
  
- **search_movie**: Permite realizar búsquedas de películas por título o director.

- **update_movie**: Permite actualizar la cantidad o el precio de una película existente.
  
- **delete_movie**: Elimina una película tras confirmar la acción por parte del usuario.

- **generate_reports**: Calcula el valor total del inventario y genera informes de las películas por género, mostrando la más antigua y la más reciente en cada género.

- **menu**: Proporciona un menú interactivo para que el usuario pueda elegir qué operación desea realizar.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `video_library_management.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo en la consola donde podrás elegir entre las diferentes opciones de gestión de películas.

### Ejemplo de flujo

1. **Registrar una película**:
   - El usuario ingresa los datos de la película (título, director, género, año, cantidad y precio).
   
2. **Buscar una película**:
   - El usuario puede buscar por título o director, y se mostrarán los resultados coincidentes.
   
3. **Actualizar una película**:
   - El usuario puede modificar la cantidad o el precio de alquiler de una película.
   
4. **Eliminar una película**:
   - El usuario puede eliminar una película después de confirmar la acción.

5. **Generar informes**:
   - El sistema muestra el valor total del inventario y la información sobre las películas más antiguas y más recientes por género.

## Objetivo

El objetivo principal de este proyecto es proporcionar una forma sencilla y eficaz de gestionar una colección de películas. Está orientado a facilitar el registro, la búsqueda y la administración de películas en un entorno de alquiler de videos, y ofrece funcionalidades básicas para monitorear el estado y el valor del inventario de películas.

## Contribuciones

Si deseas contribuir al proyecto, siéntete libre de realizar un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.
