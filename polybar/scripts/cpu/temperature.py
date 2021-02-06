import psutil
def main():
	CPU_TEMP = psutil.sensors_temperatures()['atk0110'][0][1]
	HIGH_CPU_TEMP = psutil.sensors_temperatures()['atk0110'][0][2]
	CRIT_CPU_TEMP = psutil.sensors_temperatures()['atk0110'][0][1]
	if CPU_TEMP >= HIGH_CPU_TEMP:
		print('CPU Temperature is high ' + str(CPU_TEMP)+'°C')
	elif CPU_TEMP:
		print('CPU Temperature: ' + str(CPU_TEMP)+'°C') 

if __name__ == '__main__':
	main()