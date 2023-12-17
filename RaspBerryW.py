# -----------------------Codigo para o Raspberry Ler Sensores e Calibrar-----------------------444444444

from machine import Pin, ADC, UART, time   # Importar as bibliotecas necessárias

# Definir os pinos onde os sensores estão conectados
pin_ldr = 32
pin_pressure = 33
pin_temperature = 34

# Inicializar os ADCs  --  Ver os sensores pois ADC pode depender do Hardware
adc_ldr = ADC(Pin(pin_ldr))
adc_pressure = ADC(Pin(pin_pressure))
adc_temperature = ADC(Pin(pin_temperature))

# Calibrar os ADCs
adc_ldr.atten(ADC.ATTN_11DB)
adc_pressure.atten(ADC.ATTN_11DB)
adc_temperature.atten(ADC.ATTN_11DB)

#-- Loop infinito para Ler Sensores e Imprimir -- fazer ciclo para Robot

while True:   
    # Ler os valores dos sensores
    ldr_value = adc_ldr.read()
    pressure_value = adc_pressure.read()
    temperature_value = adc_temperature.read()

    # Imprimir os valores dos sensores
    print('LDR Value: ', ldr_value)
    print('Pressure Value: ', pressure_value)
    print('Temperature Value: ', temperature_value)


# Envia "Hello Arduino" para o Arduino a cada segundo.
uart = UART(1, baudrate=9600)

while True:
    uart.write('Hello Arduino\n')
    time.sleep(1)