from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import seaborn as sns

app = Flask(__name__)

# 데이터 읽기
file_path = 'cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(file_path)

# 한글 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic.ttf'

# 함수: 성별에 따른 전체 인원 분포
def plot_gender_distribution():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sex', data=df)
    plt.title('성별 인원 분포')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

# 함수: is_recid에 따른 성별 분포
def plot_recid_gender_distribution():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sex', hue='is_recid', data=df)
    plt.title('재범 여부에 따른 성별 분포')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

# Flask 라우팅
@app.route('/')
def index():
    gender_distribution = plot_gender_distribution()
    recid_gender_distribution = plot_recid_gender_distribution()
    return render_template('index.html', gender_distribution=gender_distribution, recid_gender_distribution=recid_gender_distribution)

if __name__ == '__main__':
    app.run(debug=True)
