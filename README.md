# Proyecto_Rasberry


## 

| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | Código del Trabajo o Número de Tarea | 
| **MRG-C002** | Robótica Móvil - Bobot - Módulo 1 |

## Contenido

- [Objetivo](#objetivo)
- [Introducción](#introduccion)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)
- [Bitácora](#bitácora)


## Objetivo
Diseñar un robot omnidireccional mediante el análisis de ingeniería inversa en el DOFBOT y así obtener los parámetros de diseño para la base móvil

## Introducción
Palabras Clave
Palabras claves en forma Jerarquizada
- Diseño Mecatrónico
- Controlador de Motores
- Robot Móvil Omnidireccional
- Sistema Embebido Jerarquico
- Raspberry con ROS
- Microcontrolador
- Diseño electrónico (PCB)
- Comunicación
- Control de Velocidad


Definiendo el tema
El proyecto consta de ver el funcionamiento, adaptación e implementación de un Brazo robótico 
cuyo control será realizado en un sistema embebido Raspberry Pi y con una tarjeta de desarrollo 
programada en Arduino para adaptarlo a una base móvil omnidireccional obteniendo un manipulador móvil. 

## Desarrollo

## Conclusiones
 
## Referencias
<a id="1">[1]</a> "Choose an architecture | Download". Ubuntu MATE. https://ubuntu-mate.org/download/ (accedido el 13 de mayo de 2022).
<a id="2">[2]</a> "Noetic/Installation/Ubuntu - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/noetic/Installation/Ubuntu (accedido el 13 de mayo de 2022).
<a id="3">[3]</a> "ROS/Tutorials/CreatingPackage - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/ROS/Tutorials/CreatingPackage (accedido el 13 de mayo de 2022).
<a id="4">[4]</a> "ROS/Tutorials/BuildingPackages - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/ROS/Tutorials/BuildingPackages (accedido el 13 de mayo de 2022).
<a id="5">[5]</a> "Vision_opencv - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/vision_opencv (accedido el 13 de mayo de 2022).
<a id="6">[6]</a> "Install raspi-config on Ubuntu MATE 20.10 and higher". Ubuntu MATE Community. https://ubuntu-mate.community/t/install-raspi-config-on-ubuntu-mate-20-10-and-higher/23974 (accedido el 13 de mayo de 2022).
<a id="7">[7]</a> "How to install python3-smbus ubuntu package on ubuntu 20.04/ubuntu 18.04/ubuntu 19.04/ubuntu 16.04". Modern Server and App Hosting Control Panel. https://zoomadmin.com/HowToInstall/UbuntuPackage/python3-smbus (accedido el 13 de mayo de 2022).
<a id="8">[8]</a> "Arm_lib". PyPI. https://pypi.org/project/Arm_lib/ (accedido el 13 de mayo de 2022).
 
## Autor
| Iniciales  | Description |
| ----------:| ----------- |
| **RICF** | Felipe Rivas Campos [GitHub profile](https://github.com/rivascf) |
| **EPM**  | Erik Peña Medina [GitHub profile](https://github.com/ErikFiUNAM) |
| **DMC**  | Diego Méndez Carter [GitHub profile](https://github.com/Laos198) |
| **MGR-MX** | Mechatronics Research Group, México [GitHub profile](https://github.com/mrg-mx) |




## Bitácora

Hoy he llamado al robot "Dofbot"- por lo que me iré refiriendo
a él de desde ahora con ese nombre. 
En la Raspberry tiene las siguientes carcaterísticas:
 
	- Imagen con Raspbian Buster (legacy) 
	- Instalación de ROS Melodic

Para la instalación del sistema utilicé la siguiente WIKI
- https://www.linkedin.com/pulse/easiest-way-install-ros-melodic-raspberrypi-4-shubham-nandi
- http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi
NOTAS: 
La tarjeta arduino Uno del maestro Erik ya no funciona (al parecer) 
he dejado instalada una provisional que a veces falla. 



## 20/04/2022

Se volvió a instalar ROS en el sistema de Raspberry siguiendo los links de arriba y se establecieron las palabras claves del proyecto delimitando 
las fechas de entrega para 6 semanas. 

Palabras clave: 
- Diseño Mecatrónico
- Controlador de Motores 
- Robot Móvil Omnidireccional 
- Sistema Embebido Jerarquico 
- Raspberry con ROS 
## Punto de trabajo futuro
- Microcontrolador
- Diseño eléctrónico (PCB)
- Comunicación 
- Control de Velocidad



resolucion del problema smBus: 
https://github.com/johnbryanmoore/VL53L0X_rasp_python/issues/13
habilitando los ṕuertos i2c de la raspberry. 
https://blog.csdn.net/jcfszxc/article/details/123448078

## 27/04/2022

Se instaló OpenCV en la Raspberry y así mismo se bajo la base móvil del robot de Irene 
se quitaron Drivers MD25 y se piensa usar el por un momento los motores de estos 

Para instalar openCV y solucionar un problema con Numpy se ocuparon estas fuentes. 
https://www.piwheels.org/project/opencv-contrib-python/
https://stackoverflow.com/questions/20518632/importerror-numpy-core-multiarray-failed-to-import
https://programarfacil.com/blog/vision-artificial/opencv-raspberry-pi/


