import pandas as pd

## Load Data
print("*" * 88)
print("Load data")
print("*" * 88)

path = "melb_data.csv"
data = pd.read_csv(path)
print(f"data.describe = \n{data.describe()}")
print(f"{data.columns=}")
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[features]
y = data['Price']

print(f"X.describe = \n{X.describe()}")
print(f"X.head = \n{X.head()}")



## Build model, fit, predict
print("\n" * 5)
print("*" * 88)
print("Build model")
print("*" * 88)

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=1)  # to ensure same result always
model.fit(X, y)

print(f"y.head = \n{y.head()}")
print(f"{model.predict(X.head())=}")



# ## Check error rate
print("\n" * 5)
print("*" * 88)
print("Check error rate")
print("*" * 88)

from sklearn.metrics import mean_absolute_error as mae

predicted = model.predict(X)
print(f"{mae(y, predicted)=}")



## Split training and validation data to ensure correctness
print("\n" * 5)
print("*" * 88)
print("Split training and validation data")
print("*" * 88)
from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
model = DecisionTreeRegressor()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
print(f"{mae(val_y, val_predictions)=}")



### Prevent overfitting and underfitting by defining max_leaf_nodes
print("\n" * 5)
print("*" * 88)
print("Prevent overfitting and underfitting")
print("*" * 88)
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    return mae(val_y, preds_val)

for max_leaf_nodes in [5, 50, 500, 5_000, 50_000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {max_leaf_nodes} have mae: {my_mae}")



### Using random forest
print("\n" * 5)
print("*" * 88)
print("Random forest")
print("*" * 88)

from sklearn.ensemble import RandomForestRegressor
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
preds = forest_model.predict(val_X)
print(f"{mae(val_y, preds)=}")
