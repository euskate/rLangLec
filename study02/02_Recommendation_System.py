import pandas as pd

# 데이터 다운로드 및 로드
# MovieLens 데이터셋에서 ratings.csv와 movies.csv 파일을 다운로드해야 합니다.
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# 데이터 확인
print(ratings.head())
print(movies.head())

# 데이터 전처리 : UserID와 MovieID를 인덱스로 설정하고 평점 데이터 확인
ratings = ratings.rename(columns={'userId': 'UserID', 'movieId': 'MovieID', 'rating': 'Rating'})
movies = movies.rename(columns={'movieId': 'MovieID', 'title': 'Title'})

# 사용자-영화 평점 행렬 생성
user_movie_matrix = ratings.pivot(index='UserID', columns='MovieID', values='Rating')
print(user_movie_matrix.head())


# KNN 기반 협업 필터링
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# 사용자-영화 행렬에서 NaN 값을 0으로 대체
user_movie_matrix_filled = user_movie_matrix.fillna(0)

# 사용자 간의 유사도 계산
user_similarity = cosine_similarity(user_movie_matrix_filled)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix_filled.index, columns=user_movie_matrix_filled.index)

# 추천 함수 정의
def get_recommendations(user_id, num_recommendations=5):
    # 현재 사용자의 평점 데이터 추출
    user_ratings = user_movie_matrix.loc[user_id]
    
    # 사용자 유사도 기반 추천 영화 계산
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users[similar_users.index != user_id]
    
    # 추천 영화 계산
    recommendations = pd.Series()
    for similar_user in similar_users.index:
        similar_user_ratings = user_movie_matrix.loc[similar_user]
        recommendations = recommendations.append(similar_user_ratings)
    
    # 평점이 높은 영화 추천
    recommendations = recommendations.groupby(recommendations.index).mean()
    recommendations = recommendations[~user_ratings.isna()]
    recommendations = recommendations.sort_values(ascending=False)
    
    return recommendations.head(num_recommendations)

# 사용자 ID 1에게 5개의 영화 추천
print(get_recommendations(1, num_recommendations=5))

# 장르 기반 추천
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 장르 정보를 TF-IDF 벡터로 변환
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['genres'])

# 코사인 유사도 계산
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 영화 제목을 인덱스로 설정
indices = pd.Series(movies.index, index=movies['Title']).to_dict()

# 추천 함수 정의
def content_based_recommendations(title, num_recommendations=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['Title'].iloc[movie_indices]

# 'The Dark Knight' 영화와 유사한 5개의 영화 추천
print(content_based_recommendations('The Dark Knight', num_recommendations=5))

# 추천 결과 시각화
import matplotlib.pyplot as plt

# 협업 필터링 추천 결과 시각화
recommendations = get_recommendations(1, num_recommendations=5)
plt.figure(figsize=(10, 6))
recommendations.plot(kind='bar')
plt.title('Top 5 Movie Recommendations Based on Collaborative Filtering')
plt.xlabel('Movie')
plt.ylabel('Average Rating')
plt.show()

# 콘텐츠 기반 추천 결과 시각화
content_recommendations = content_based_recommendations('The Dark Knight', num_recommendations=5)
print("Content-Based Recommendations:")
print(content_recommendations)