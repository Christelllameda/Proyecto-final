# **Proyecto Final - Obras públicas inconclusas en Venezuela** </div>
[![edit-1.jpg](https://i.postimg.cc/vBRN0Lrb/edit-1.jpg)](https://postimg.cc/v1zhBn2N)
---
</div>

## Introducción
En el presente proyecto hablaremos sobre las obras públicas inconclusas en Venezuela. Este proyecto es una iniciativa estratégica diseñada para abordar los desafíos en la ejecución y seguimiento de obras de infraestructura en el país. Similar a otros lugares en el mundo, Venezuela enfrenta dificultades que afectan el desarrollo y bienestar de sus ciudadanos debido a la falta de conclusión de proyectos públicos.

El objetivo central de este proyecto es analizar y visualizar datos relacionados con obras públicas que se encuentran actualmente inconclusas en diversas regiones de Venezuela. La ejecución de obras inconclusas puede tener consecuencias significativas, incluido el desperdicio de recursos públicos, la falta de acceso a servicios esenciales para la población y un impacto negativo en la calidad de vida de las comunidades afectadas.

Para mejorar la comprensión y visibilidad de estos datos, se utilizará la plataforma de visualización de datos Tableau. Esta herramienta permitirá presentar de manera interactiva y gráfica la información recopilada, destacando patrones, tendencias y áreas críticas. La visualización de datos en Tableau facilitará la identificación de áreas geográficas específicas con un alto número de obras inconclusas, la distribución de los recursos asignados y otros indicadores clave.

Al emplear Tableau, se espera proporcionar a las partes interesadas, responsables de la toma de decisiones y al público en general, una comprensión más clara y accesible de la situación de las obras públicas inconclusas en Venezuela. Esto, a su vez, puede contribuir a la formulación de políticas más informadas, la asignación eficiente de recursos y la implementación de soluciones efectivas para abordar esta problemática. La visualización de datos en Tableau será una herramienta valiosa para promover la transparencia y el entendimiento público de la situación de las obras públicas en el país.


## Contenido
- [data](https://github.com/Christelllameda/Proyecto-final/tree/main/data)
- [jupyter notebook](https://github.com/Christelllameda/Proyecto-final/tree/main/jupyter%20notebook)
- [src](https://github.com/Christelllameda/Proyecto-final/tree/main/src)
- [img](https://github.com/Christelllameda/Proyecto-final/tree/main/img)


## Objetivos
El propósito final de este proyecto es proporcionar a los ciudadanos, funcionarios gubernamentales y la sociedad civil una herramienta valiosa para el monitoreo y la toma de decisiones informadas en relación con las obras públicas en Venezuela. Al aumentar la transparencia y visibilidad de estas obras, se busca contribuir a la mejora de la gestión de proyectos de infraestructura y, en última instancia, al desarrollo sostenible del país.
Para ello necesitaremos:

Identificar las obras públicas inconclusas en los diferentes sectores.

Definir el valor total de las obras públicas que no se han terminado de ejecutar.

## Extracción y limpieza de datos
Para el proceso de ETL nos basamos en la extracción de datos de dos fuentes distintas, en este caso fueron dos páginas webs y la Api Geopy que nos proporcionó las coordenadas de las diferentes direcciones de las obras.

Los métodos de extracción fueron: web scraping (selenium) donde obtuvimos todos los datos de las obras (status, dirección, el valor total de la obra, fecha de inicio, etc). Además utilizamos un cvs que contenía todos lo estados de Venezuela junto con su población y densidad.

Los procesos anteriores se realizaron para crear un conjunto de datos completos y actualizados sobre estas obras. Luego, se llevó a cabo una limpieza y transformación de los datos para estandarizar la información y hacerla más accesible y comprensible. 

## Creación de base de datos
Para la creación de nuestra base de datos utilizamos MySQL desde python, para ello efectuamos la conexión al servidor para crear una nueva base de datos vacía a la que llamamos 'total_obras".

Posteriormente cargamos nuestro archivo como un dataframe y ejecutamos el comando '.to_sql" para crear una nueva tabla llamada "obras_inconclusas" que contiene todas las obras en los distintos sectores que scrapeamos. Todo los códigos se encuentran descritos en el jupyter notebook 'Base_datos_sql'

## Visualización de datos
En el proceso de visualización de datos, nos basamos en el archivo 'obras_inconclusas.xlsx' que contiene todos los datos extraídos de las diferentes obras. Para llevar a cabo esta tarea de manera efectiva y dinámica, hemos empleado Tableau, una herramienta especializada en la creación de visualizaciones interactivas.

Tableau nos ha permitido explorar y presentar de manera clara y comprensible los patrones y detalles inherentes a las obras públicas inconclusas en Venezuela. A través de diversas visualizaciones, hemos delineado tendencias, identificado áreas críticas y proporcionado una visión integral de la situación de estas obras. Este enfoque visual no solo mejora la comprensión de los datos, sino que también facilita la toma de decisiones informadas.

La utilización de Tableau ha posibilitado la creación de un dashboard interactivo que permite a los usuarios explorar los datos de manera personalizada. Desde la identificación de proyectos específicos hasta el análisis de ejecución financiera, la visualización de datos en Tableau se erige como una herramienta valiosa para todos los interesados, desde responsables de proyectos hasta ciudadanos preocupados por el desarrollo de su comunidad.

En el siguiente link se visualiza el resultado final del dashboard

(https://public.tableau.com/app/profile/christell.lameda/viz/Obras_inconclusas_vzla/Dashboard1?publish=yes)


## Conclusión
El presente proyecto es una iniciativa crucial para abordar la problemática de las obras inconclusas de infraestructura en el país. A través de la recopilación, limpieza, análisis y visualización de datos, este proyecto busca aumentar la transparencia y la toma de decisiones informadas en relación con las obras públicas inconclusas. Al hacerlo, contribuye al mejoramiento de la gestión de proyectos de infraestructura y, en última instancia, al desarrollo sostenible de Venezuela. La identificación de obras inconclusas y su análisis detallado son pasos fundamentales hacia un futuro en el que los recursos públicos se utilicen eficaz y eficientemente para el beneficio de la sociedad.

Una vez realizada la extracción y posterior visualización de datos, se obtuvo un total de 60 obras públicas sin finalizar, el sector con mas obras es el de transporte pero el sector de hidrocarburos es en el que mas cantidad de dinero se ha gastado, el estado es Carabobo  y una cantidad de 185.478,78 millones de dólares invertidos.

## Links & Recursos
- https://pandas.pydata.org/
- https://docs.python.org/3/library/functions.html
- https://geopy.readthedocs.io/en/latest/
- https://selenium-python.readthedocs.io/
- https://help.tableau.com/current/pro/desktop/es-es/environment_workspace.htm
- https://dev.mysql.com/doc/workbench/en/