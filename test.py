import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic.ttf'

# CSV 파일에서 데이터 읽기
file_path = 'cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(file_path)

# 나머지 코드는 이전과 동일합니다.

# 나이 카테고리 추가
df['age_cat'] = pd.cut(df['age'], bins=[0, 25, 45, 100], labels=['Less than 25', '25 - 45', 'Greater than 45'])

# 성별에 따른 전체 인원 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', data=df)
plt.title('성별 인원 분포')
plt.show()

# 나이 카테고리에 따른 전체 인원 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='age_cat', data=df)
plt.title('나이 분포')
plt.show()

# 인종에 따른 전체 인원 분포
plt.figure(figsize=(12, 6))
sns.countplot(x='race', data=df)
plt.title('인종 분포')
plt.show()

# 이전 범죄 기록이 있는 경우의 인원 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='priors_count', data=df[df['priors_count'] > 0])
plt.title('범죄 기록 분포')
plt.show()

# is_recid에 따른 성별 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', hue='is_recid', data=df)
plt.title('재범 여부에 따른 성별 분포')
plt.show()

# is_recid에 따른 나이 카테고리 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='age_cat', hue='is_recid', data=df)
plt.title('재범 여부에 따른 나이 카테고리 분포')
plt.show()

# is_recid에 따른 인종 분포
plt.figure(figsize=(12, 6))
sns.countplot(x='race', hue='is_recid', data=df)
plt.title('재범 여부에 따른 인종 분포')
plt.show()

# is_recid에 따른 이전 범죄 기록 분포
plt.figure(figsize=(8, 6))
sns.countplot(x='priors_count', hue='is_recid', data=df[df['priors_count'] > 0])
plt.title('재범 여부에 따른 범죄 기록 분포')
plt.show()
