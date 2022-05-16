## LINEAMIENTOS PARA INSTALAR ROS EN RASPBERRY PI 4/ 4GB RAM

Se necesitará :  
- Raspberry pi 4 de 4-8gb ram 
- Adapatador de SD para PC
- Memoria sd clase 10 con 32gb de almacenamiento (mínimo) 
- Fuente de 5v 3Amp 
- Monitor 
- Cable HDMI - HDMI mini
- Teclado (USB) 
- Mouse (USB)

Como el objetivo del proyecto es trabajar con ROS Noetic (y en futuro migrar a ROS2), se optó utilizar una distribución de ubuntu con una interfaz gráfica amigable que soportara dicha versión y LTS. 
En este caso UBUNTU Mate 20.04 para tiene una distribución para la RaspBerry (RB) en donde el middleware es instalable con soporte hasta el 2023 (se utilizó la versión de 64 bits). 

La descarga y las especificacioens del sistema se pueden visualizar en la página de UBUNTU Mate ligada a la siguiente referencia [[1]](#1)
![image](https://user-images.githubusercontent.com/20031100/168504202-2b1ba9af-53c8-4d7e-afe7-20bcbc41ad4f.png)

1) Con la imagen del sistema descargada se requiería montar la imagen del sistema y la comunidad de RB tiene un montador de imagénes disponible para esta tarea, el cual solamente se debe instalar y seleccionar la imagen de UBUNTU Mate insertando la sd con un adaptador [[2]](#2)

![image](https://user-images.githubusercontent.com/20031100/168504728-dd58fe38-1a89-44d0-b0cc-98bc4ec656cb.png)

2) Después de hacer toda la configuración de la RB con UBUNTU Mate, se deben bloquear las actualizaciones de los Drivers de Bluethoot ya que se han reportado que existen bugs al momento de hacerlo, de preferencia solo hacerlo con la interfaz gráfica de paquetes. 

3) Para este paso, ya se está listo para instalar el middleware, para ello se utilizó como referencia la Wiki de ROS para la versión Noetic  [[3]](#3)


<a id="1">[1]</a> "Choose an architecture | Download". Ubuntu MATE. https://ubuntu-mate.org/download/ (accedido el 13 de mayo de 2022).
<a id="2">[2]</a>"Raspberry pi OS â raspberry pi". Raspberry Pi. https://www.raspberrypi.com/software/ (accedido el 16 de mayo de 2022).
<a id="3">[3]</a> "Noetic/Installation/Ubuntu - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/noetic/Installation/Ubuntu (accedido el 13 de mayo de 2022).
