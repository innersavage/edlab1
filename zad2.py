from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas

print('W pocie czoła ładuję dane...')
sample_dataset = datasets.load_wine()

x_train, x_test = train_test_split(sample_dataset.data, test_size=0.4)
y_train = y_test = sample_dataset.feature_names

train_pandas = pandas.DataFrame(data=x_train, columns=y_train)
test_pandas = pandas.DataFrame(data=x_test, columns=y_test)

train_pandas.to_csv('out/train.csv', sep=',', float_format='%.3f')
test_pandas.to_csv('out/test.csv', sep=',', float_format='%.3f')
