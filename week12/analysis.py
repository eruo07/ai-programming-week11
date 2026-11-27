import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "scores_2026.csv"
df = pd.read_csv(csv_path)


def 정제(df):
    """점수와 중복 조건에 맞게 데이터프레임을 정제한다."""
    결과 = df.copy()  # 원본 데이터를 직접 변경하지 않고 복사본을 만든다

    결과 = 결과.dropna(subset=["점수"])
    print(len(결과))  # 빈 점수를 제거한 뒤 남은 행 수를 출력한다

    결과 = 결과.drop_duplicates()
    print(len(결과))  # 완전히 같은 행을 하나만 남긴 뒤 행 수를 출력한다

    결과["반"] = 결과["반"].str.strip()
    결과["과목"] = 결과["과목"].str.strip()
    print(len(결과))  # 반과 과목의 앞뒤 공백을 제거한 뒤 행 수를 출력한다

    결과 = 결과[(결과["점수"] >= 0) & (결과["점수"] <= 100)]
    print(len(결과))  # 유효하지 않은 점수 행을 제거한 뒤 행 수를 출력한다

    return 결과

if __name__ == "__main__":
    폴더 = __file__[:-len("analysis.py")]
    df = pd.read_csv(폴더 + "scores_2026.csv")
    df = 정제(df)
    print(df.shape)  # (114, 5)
    print(df["점수"].isna().sum())  # 빈 칸이 몇 개인가
    print(df.duplicated().sum())  # 완전히 같은 행이 몇 개인가
    print(df["반"].unique())  # 반 값에 앞뒤 공백이 섞여 있는지 확인한다
    print(df["과목"].unique())  # 과목 값에 앞뒤 공백이 섞여 있는지 확인한다
    print(df["점수"].describe())  # 점수의 범위와 이상치가 있는지 확인한다

정제(df)



# analysis.py 파일 맨 아래에 추가
수학_df = df[df["과목"] == "수학"]
print(수학_df.shape[0])  # 과목이 '수학'인 행의 수

# '반'으로 묶어 점수 평균 계산
반별_점수_평균 = df.groupby("반")["점수"].mean()
print(반별_점수_평균)

# '과목'과 '반' 두 기준으로 묶는 코드
과목_및_반별_점수_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목_및_반별_점수_평균)

# '반'으로 묶어 개수, 평균, 중앙값, 최댓값
반별_통계 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"])
print(반별_통계.round(2))
