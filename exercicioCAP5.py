import pandas as pd


# 1)
df = pd.read_csv('paises.csv', delimiter=';')
oceania_data = df[df['Region'].str.contains('OCEANIA')] 
oceania_countries = oceania_data[['Country', 'Region']] 
print(oceania_countries)
print('Contagem: ', oceania_countries.count()[1])

# 2)
taxa = df['Literacy (%)'].sum()/df['Literacy (%)'].count()
print('Média da taxa de alfabetização: ', taxa, '%')

# 3)
argumentoNome = df['Pop. Density (per sq. mi.)'].argmax() 
print('Nome do Pais:', df.iloc[argumentoNome, 0], ' Região do pais: ', df.iloc[argumentoNome, 1])

# 4)
paisesZero = df[df['Coastline (coast/area ratio)'] == 0]
paisesZero['Country'].to_csv('noCoast.csv', sep=';', header=False)

