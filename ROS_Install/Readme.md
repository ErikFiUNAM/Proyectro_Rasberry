# LINEAMIENTOS PARA INSTALAR ROS EN RASPBERRY PI 4/ 4GB RAM

## Materiales 
Se necesitará :  
- Raspberry pi 4 de 4-8gb ram 
- Adapatador de SD para PC
- Memoria sd clase 10 con 32gb de almacenamiento (mínimo) 
- Fuente de 5v 3Amp 
- Monitor 
- Cable HDMI - HDMI mini
- Teclado (USB) 
- Mouse (USB)

## Instrucciones para instalar Ubuntu Mate RaspBerry 
Como el objetivo del proyecto es trabajar con ROS Noetic (y en futuro migrar a ROS2), se optó utilizar una distribución de ubuntu con una interfaz gráfica amigable que soportara dicha versión y LTS. 
En este caso UBUNTU Mate 20.04 para tiene una distribución para la RaspBerry (RB) en donde el middleware es instalable con soporte hasta el 2023 (se utilizó la versión de 64 bits). 

La descarga y las especificacioens del sistema se pueden visualizar en la página de UBUNTU Mate ligada a la siguiente referencia [[1]](#1)
![image](https://user-images.githubusercontent.com/20031100/168504202-2b1ba9af-53c8-4d7e-afe7-20bcbc41ad4f.png)

1) Con la imagen del sistema descargada se requiería montar la imagen del sistema y la comunidad de RB tiene un montador de imagénes disponible para esta tarea, el cual solamente se debe instalar y seleccionar la imagen de UBUNTU Mate insertando la sd con un adaptador [[2]](#2)

![image](https://user-images.githubusercontent.com/20031100/168504728-dd58fe38-1a89-44d0-b0cc-98bc4ec656cb.png)

2) Después de hacer toda la configuración de la RB con UBUNTU Mate, se deben bloquear las actualizaciones de los Drivers de Bluethoot ya que se han reportado que existen bugs al momento de hacerlo, de preferencia solo hacerlo con la interfaz gráfica de paquetes. 

# Instalación de ROS
3) Aquí ya podemos empezar la instalación del middleware, para ello se utilizó como referencia la Wiki de ROS para la versión Noetic  [[3]](#3)
![image](https://user-images.githubusercontent.com/20031100/168505727-d3e0ff8c-7c7b-46b4-be3c-4be1eea5d205.png)

o Configuración del "sources.list"
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
o Instlar las Keys de ROS
```
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

o Instalación 
  - Actualización de los paquetes de Debian: 
```
sudo apt update
```
o Seleccionando la instalación
Como solo necesitamos los elementos básicos para que corra de la forma más ligera posible dentro de la RB, se optó por ROS - Base que no incluye los paquetes de simulación y percepción, solo algunos paquetes y bibliotecas de comunicación.

```
sudo apt install ros-noetic-ros-base
```

o Configuracipon del Ambiente 
se debe hacer "source" en cada terminal en el cual se vaya a utlizar ROS con el siguiente comando: 

```
source /opt/ros/noetic/setup.bash
```

o Dependencias para construir los paquetes

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```


```
sudo apt install python3-rosdep
```

```
sudo rosdep init
rosdep update
```

- En este momento ya estaríamos listos para poder verificar que ROS Noetic esté bien instalado corriendo el siguiente comando: 
```
roscore
```

# Creando un WS en ROS 




<a id="1">[1]</a> "Choose an architecture | Download". Ubuntu MATE. https://ubuntu-mate.org/download/ (accedido el 13 de mayo de 2022).

<a id="2">[2]</a>"Raspberry pi OS â raspberry pi". Raspberry Pi. https://www.raspberrypi.com/software/ (accedido el 16 de mayo de 2022).

<a id="3">[3]</a> "Noetic/Installation/Ubuntu - ROS wiki". Documentation - ROS Wiki. http://wiki.ros.org/noetic/Installation/Ubuntu (accedido el 13 de mayo de 2022).
