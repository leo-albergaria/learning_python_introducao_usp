segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = ((segundos % 86400) % 3600) // 60
segundos = ((segundos % 86400) % 3600) % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

