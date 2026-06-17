from google_play_scraper import Sort, reviews
import pandas as pd

app_id = 'com.chess'
total_data_target = 20000
data_ulasan = []
token = None

while len(data_ulasan) < total_data_target:
    result, token = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=1000, 
        continuation_token=token
    )
    data_ulasan.extend(result)

df = pd.DataFrame(data_ulasan)
df = df.drop_duplicates(subset=['content'])
df = df[['userName', 'score', 'at', 'content']]
df = df.head(20000)
df.to_csv('chess_reviews.csv', index=False, encoding='utf-8')
print(f"Done! Total data: {len(df)}")