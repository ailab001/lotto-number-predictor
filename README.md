# 🎰 로또 번호 예측기 (Lotto Number Predictor)

한국 로또 645의 과거 당첨 번호를 분석하여 다양한 알고리즘으로 번호를 예측하는 Python 프로그램입니다.

A Python program that analyzes past winning numbers of Korean Lotto 6/45 and predicts numbers using various algorithms.

---

## ✨ 주요 기능 (Features)

### 📊 데이터 분석
- 동행복권 공식 API에서 실시간 당첨 번호 조회
- 번호별 출현 빈도 통계
- 홀수/짝수 비율 분석
- TOP/BOTTOM 번호 분석

### 🎯 예측 알고리즘
1. **빈도수 기반 예측**: 가장 많이 나온 번호 중심
2. **콜드 넘버 예측**: 적게 나온 번호 중심 (반전 가능성)
3. **균형 예측**: 홀짝/고저 번호 균형 배치
4. **최근 트렌드 예측**: 최근 회차 트렌드 반영
5. **랜덤 예측**: 완전 무작위 선택

---

## 🚀 빠른 시작 (Quick Start)

### 1️⃣ 저장소 복제
```bash
git clone https://github.com/your-username/lotto-number-predictor.git
cd lotto-number-predictor
```

### 2️⃣ 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

또는

```bash
pip install requests
```

### 3️⃣ 실행
```bash
python lotto_predictor.py
```

---

## 📖 사용 방법 (How to Use)

### 기본 실행
프로그램을 실행하면 자동으로:
1. 최근 100회차의 로또 데이터를 가져옵니다
2. 통계 분석을 수행합니다
3. 5가지 방법으로 번호를 예측합니다

### 고급 사용법
Python 코드에서 직접 사용할 수 있습니다:

```python
from lotto_predictor import LottoPredictor

# 예측기 생성
predictor = LottoPredictor()

# 데이터 로드 (1회차부터 최신 회차까지)
predictor.fetch_lotto_data(1, None)

# 특정 방법으로 예측
numbers = predictor.predict_by_frequency()
print(f"예측 번호: {numbers}")

# 통계 확인
predictor.show_statistics()

# 여러 세트 생성
predictions = predictor.generate_predictions(num_sets=10)
```

---

## 📊 실행 예시 (Example Output)

```
╔═══════════════════════════════════════╗
║     🎱 로또 번호 예측기 v1.0 🎱      ║
╚═══════════════════════════════════════╝

로또 데이터를 가져오는 중...
총 100회차 데이터 로드 완료!

============================================================
📊 로또 통계 분석
============================================================

[TOP 10 자주 나온 번호]
 1. 번호 34: 15회 출현
 2. 번호 17: 14회 출현
 ...

============================================================
🎰 로또 번호 예측 결과
============================================================

[1번 세트 - 빈도수 기반]
번호:  7 12 17 23 34 43

[2번 세트 - 콜드 넘버]
번호:  2  9 14 28 31 42

...
```

---

## 🛠️ 기술 스택 (Tech Stack)

- **Python 3.6+**
- **requests**: HTTP 요청 라이브러리
- **동행복권 공식 API**: 실시간 당첨 번호 데이터

---

## 📁 프로젝트 구조 (Project Structure)

```
lotto-number-predictor/
├── lotto_predictor.py    # 메인 프로그램
├── requirements.txt       # 필요한 패키지 목록
├── README.md             # 프로젝트 설명
└── .gitignore           # Git 제외 파일 목록
```

---

## 🔧 커스터마이징 (Customization)

### 데이터 범위 변경
```python
# 전체 회차 데이터 로드
predictor.fetch_lotto_data(1, None)

# 특정 범위만 로드
predictor.fetch_lotto_data(1000, 1100)
```

### 예측 세트 개수 변경
```python
# 10개의 번호 세트 생성
predictions = predictor.generate_predictions(num_sets=10)
```

### 최근 트렌드 분석 기간 변경
```python
# 최근 20회차 기준으로 예측
numbers = predictor.predict_by_recent_trend(recent_rounds=20)
```

---

## ⚠️ 주의사항 (Disclaimer)

- 이 프로그램은 **재미와 학습 목적**으로 제작되었습니다
- 로또는 **순수한 확률 게임**이며, 모든 번호는 동일한 당첨 확률을 가집니다
- 예측 결과는 **참고용**이며, 당첨을 보장하지 않습니다
- 과도한 복권 구매는 경제적 어려움을 초래할 수 있습니다
- 책임있는 구매를 권장합니다

---

## 🤝 기여하기 (Contributing)

버그 리포트, 기능 제안, Pull Request를 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 라이선스 (License)

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

---

## 📞 문의 (Contact)

프로젝트 관련 문의사항이 있으시면 Issue를 등록해주세요.

---

## 🍀 행운을 빕니다!

**Remember: 로또는 재미로, 투자는 신중하게!**

---

## 📈 업데이트 내역 (Changelog)

### v1.0.0 (2026-10-30)
- 초기 릴리스
- 5가지 예측 알고리즘 구현
- 통계 분석 기능
- 동행복권 API 연동
