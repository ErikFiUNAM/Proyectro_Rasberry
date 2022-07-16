# CheatSheet del protocolo I2C


## Definición

- [Definición](#definicion)
- [Bus I2C en RBP](#)
- [Bus_I2C en Arduino](#)
- [Bus I2C en NODEMCU](#)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)

## Definición

Inter Integrated Circuit, es un bus serie desarrollado por Phillips semiconductors ampliamente utilizado en la industria electrónica. Está formado por dos hilos que puede conectar varios dispositivos mediante un hardware sencillo (como se muestra en la siguiente imagen) 

![image](https://user-images.githubusercontent.com/20031100/172984479-cdf5ca22-ab79-4b45-9e5f-5ffd2f11864d.png)

Por los dos Hilos se produce la comunicación serie, bit a bit (unidad mínima de información). 
Donde:

- SCL, (Serial Clock) Es una señal de reloj que se utiliza para la sincronización
    
- SDA (Serial Data) Es la línea para la transferencia serie de Datos 
    
    
Los dispositivos concetados en el Bus I2C mantiene una relación entre ellos de maestro/esclavo: 

- El maestro inicia y termina la transferencia de información, además de controlar la señal de reloj (Generalmente es un Microcontrolador, pero en este caso será la RaspBerry) 
- El esclavo es el circiuto direccionado por le maestro

La línea SDA es bidireccional, por lo que el maestro y el esclavo actúan como transmisores o receptores de datos.

Es necesario considerar que dentro del cableado del circuito será prudente utilizar dos resistencias en configuración Pull-Up ya que dos o más señales a través del mismo cable pueden causar conflicto.

Se pueden conectar 128 dispositivos a la vez ya que las direcciones que maneja el BUS son de 7 bits. Aunque este tiene reservado 16 direccioens por lo que al final se pueden usar un máximo de 112 nodos entre sí. 



## Bus I2C en RBP

## Bus I2C en Arduino

## Bus I2C en NODEMCU






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
| **DMC**  | Diego Méndez Carter [GitHub profile](https://github.com/Laos198) |
| **MGR-MX** | Mechatronics Research Group, México [GitHub profile](https://github.com/mrg-mx) |

