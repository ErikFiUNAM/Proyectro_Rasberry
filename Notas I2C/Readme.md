# CheatSheet del protocolo I2C


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
