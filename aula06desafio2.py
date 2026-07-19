n = input('Digite algo')
print(f'É um número? {n.isnumeric()}')
print('É uma(s) letra(s)?', n.isalpha())
print('É um alfanumérico?', n.isalnum())
print('É um decimal?', n.isdecimal())
print('Só tem espaços?', n.isspace())
print('É um dígito?', n.isdigit())
print('Só tem letras maiúsculas?', n.isupper())
print('Só tem letras minúsculas?', n.islower())

# O a é o que nós chamamos de "objeto". Todo objeto tem características e realiza funcionlaidades.