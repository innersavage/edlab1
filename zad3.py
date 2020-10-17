import pandas

print('W pocie czoła ładuję dane (tym razem z plików)...')
train_set = pandas.read_csv('out/train.csv', sep=',')
test_set = pandas.read_csv('out/test.csv', sep=',')

for dataset, dataset_name in [(train_set, 'Zbiór treningowy'), (test_set, 'Zbiór testowy')]:
    print('Analiza ilościowa dla: {}'.format(dataset_name))
    for label in dataset.columns[1:]:
        print('Dla etykiety: {}'.format(label))
        print('Ilość wartości: {}'.format(dataset.count()[label]))
        print('Ilość wartości unikatowych: {}'.format(len(dataset[label].unique())))
        print('Wartość średnia w zbiorze: {}'.format(dataset[label].mean()))
        print('Ilość wartości null: {}'.format(dataset[label].isna().sum()))
        print('Wartość maksymalna: {}'.format(dataset.max()[label]))
        print('Wartość minimalna: {}'.format(dataset.min()[label]))
        print('Wartość najczęściej występująca w zbiorze: {}'.format(dataset[label].mode().max()))
        print()
    print()
