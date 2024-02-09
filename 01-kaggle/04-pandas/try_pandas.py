import pandas as pd

print('*' * 88)
print('Creating Dataframe and series')
print('*' * 88)

df = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print(f"df=\n{df}")
df = pd.DataFrame(
    {
        "Bob": ["I like it.", "It was awful."],
        "Sue": ["Pretty good.", "Bland."]
    },
    index=["Product A", "Product B"]
)
print(f"df=\n{df}")

series = pd.Series([1, 2, 3, 4, 5])
print(f"series=\n{series}")

series = pd.Series(
    [30, 35, 40],
    index=["2015 Sales", "2016 Sales", "2017 Sales"],
    name="Product A"
)
print(f"series=\n{series}")

print('\n' * 8)
print('*' * 88)
print('Read csv')
print('*' * 88)
reviews = pd.read_csv("wine-data.csv", index_col=0)
features = ['country', 'province', 'designation', 'title', 'points', 'price', 'taster_name']
reviews = reviews[features]
print(reviews.shape)
print(reviews.head())
print(reviews.country)

print(reviews.loc[0])
print(reviews.iloc[0])
new_reviews = reviews.set_index('title')
print(new_reviews.head())


print('\n' * 8)
print('*' * 88)
print('Querying')
print('*' * 88)

italian_wines = reviews.loc[reviews['country'] == 'Italy']
print(italian_wines)

italian_wines_with_90_plus_points = (
    reviews.loc[
        (reviews['country'] == 'Italy')  # parentheses is a must because operator precedence
        & (reviews['points'] >= 90)
    ]
)
print(italian_wines_with_90_plus_points)

italian_or_france_wines = (
    reviews.loc[reviews['country'].isin(['France', 'Italy'])]
)
print(italian_or_france_wines)

wines_with_price = reviews.loc[reviews['price'].notnull()]
print(wines_with_price)

print(reviews.loc[reviews['points'] < 90])


print('\n' * 8)
print('*' * 88)
print('Assigning data')
print('*' * 88)

reviews['critics'] = 'Everyone'
print(reviews)
reviews['index_backward'] = range(len(reviews), 0, -1)
print(reviews)


print('\n' * 8)
print('*' * 88)
print('Get Summary')
print('*' * 88)

print(reviews.points.describe)
print(reviews.taster_name.describe)


print('\n' * 8)
print('*' * 88)
print('Map and apply')
print('*' * 88)

review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

print(reviews.apply(remean_points, axis='columns').points)
print(reviews.points)  # it doesn't modify in place


print('\n' * 8)
print('*' * 88)
print('Grouping and sorting')
print('*' * 88)

print(reviews.groupby('points').points.count())
print(reviews.groupby('points').price.min())
print(reviews.groupby(['country', 'province']).apply(lambda x: x.loc[x.points.idxmax()]))

len_min_max_reviews = reviews.groupby(['country']).price.agg([len, min, max])
print(len_min_max_reviews)

len_min_max_reviews.sort_values(by='min', ascending=False)


print(reviews.dtypes)

print(reviews[reviews['country'].isnull()])
print(reviews[reviews['country'].isnull()].fillna('Unknown'))
print(reviews[reviews['country'].isnull()].fillna('Unknown').replace('Unknown', 'Potato'))

reviews.rename(columns={'points': 'score'})
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
