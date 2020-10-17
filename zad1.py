from sklearn import datasets

print('W pocie czoła ładuję dane...')
sample_dataset = datasets.load_wine()
print('A teraz analiza...')

print('Description zbioru:\n{}'.format(sample_dataset['DESCR']))
print('Próbki:\n{}'.format(sample_dataset.target))
print('Cechy:\n{}'.format(sample_dataset.feature_names))
print('Nazwy klas:\n{}'.format(sample_dataset.target_names))
print('Trochę danych (pandas DataFrame):\n{}'.format(sample_dataset['data']))