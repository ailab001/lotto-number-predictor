#!/usr/bin/env python3
"""
한국 로또 번호 예측기
과거 당첨 번호를 분석하여 다양한 방법으로 로또 번호를 예측합니다.
"""

import requests
import random
from collections import Counter
from datetime import datetime
import json
import os


class LottoPredictor:
    """로또 번호 예측 클래스"""

    def __init__(self):
        self.base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
        self.history = []
        self.all_numbers = []

    def fetch_lotto_data(self, start_round=1, end_round=None):
        """
        로또 당첨 번호 데이터를 가져옵니다.

        Args:
            start_round: 시작 회차
            end_round: 종료 회차 (None이면 최신 회차까지)
        """
        print("로또 데이터를 가져오는 중...")

        if end_round is None:
            # 최신 회차 확인
            response = requests.get(f"{self.base_url}1")
            if response.status_code == 200:
                data = response.json()
                if data['returnValue'] == 'success':
                    # 대략적인 최신 회차 추정 (매주 토요일 추첨)
                    weeks_since_start = (datetime.now() - datetime(2002, 12, 7)).days // 7
                    end_round = min(weeks_since_start, 1200)  # 안전하게 제한

        for round_num in range(start_round, end_round + 1):
            try:
                response = requests.get(f"{self.base_url}{round_num}")
                if response.status_code == 200:
                    data = response.json()
                    if data['returnValue'] == 'success':
                        numbers = [
                            data['drwtNo1'], data['drwtNo2'], data['drwtNo3'],
                            data['drwtNo4'], data['drwtNo5'], data['drwtNo6']
                        ]
                        bonus = data['bnusNo']

                        self.history.append({
                            'round': round_num,
                            'numbers': numbers,
                            'bonus': bonus,
                            'date': data['drwNoDate']
                        })
                        self.all_numbers.extend(numbers)

                        if round_num % 100 == 0:
                            print(f"{round_num}회차까지 조회 완료...")
                    else:
                        break
            except Exception as e:
                print(f"{round_num}회차 조회 실패: {e}")
                break

        print(f"총 {len(self.history)}회차 데이터 로드 완료!\n")

    def get_frequency_analysis(self):
        """번호별 출현 빈도 분석"""
        counter = Counter(self.all_numbers)
        return counter.most_common()

    def predict_by_frequency(self, count=6):
        """
        빈도수 기반 예측
        가장 많이 나온 번호들 중에서 선택
        """
        if not self.all_numbers:
            return self.predict_random(count)

        freq = self.get_frequency_analysis()
        top_numbers = [num for num, _ in freq[:15]]  # 상위 15개 중에서
        if len(top_numbers) < count:
            return self.predict_random(count)
        return sorted(random.sample(top_numbers, count))

    def predict_by_cold_numbers(self, count=6):
        """
        콜드 넘버 기반 예측
        적게 나온 번호들 중에서 선택 (반전 가능성)
        """
        if not self.all_numbers:
            return self.predict_random(count)

        freq = self.get_frequency_analysis()
        cold_numbers = [num for num, _ in freq[-20:]]  # 하위 20개 중에서
        if len(cold_numbers) < count:
            return self.predict_random(count)
        return sorted(random.sample(cold_numbers, count))

    def predict_by_balanced(self, count=6):
        """
        균형 예측
        홀수/짝수, 고저 번호를 균형있게 선택
        """
        numbers = set()

        # 홀수 3개, 짝수 3개 목표
        odd_numbers = [n for n in range(1, 46) if n % 2 == 1]
        even_numbers = [n for n in range(1, 46) if n % 2 == 0]

        numbers.update(random.sample(odd_numbers, 3))
        numbers.update(random.sample(even_numbers, 3))

        return sorted(list(numbers))

    def predict_by_recent_trend(self, count=6, recent_rounds=10):
        """
        최근 트렌드 기반 예측
        최근 N회차에서 자주 나온 번호 중심
        """
        if not self.history:
            return self.predict_random(count)

        recent_numbers = []
        for draw in self.history[-recent_rounds:]:
            recent_numbers.extend(draw['numbers'])

        counter = Counter(recent_numbers)
        top_numbers = [num for num, _ in counter.most_common(12)]

        if len(top_numbers) < count:
            return self.predict_random(count)

        return sorted(random.sample(top_numbers, count))

    def predict_random(self, count=6):
        """완전 랜덤 예측"""
        return sorted(random.sample(range(1, 46), count))

    def generate_predictions(self, num_sets=5):
        """
        여러 예측 방법을 사용하여 번호 세트 생성

        Args:
            num_sets: 생성할 번호 세트 개수
        """
        print("=" * 60)
        print("🎰 로또 번호 예측 결과")
        print("=" * 60)

        predictions = []
        methods = [
            ("빈도수 기반", self.predict_by_frequency),
            ("콜드 넘버", self.predict_by_cold_numbers),
            ("균형 예측", self.predict_by_balanced),
            ("최근 트렌드", self.predict_by_recent_trend),
            ("랜덤", self.predict_random)
        ]

        for i in range(num_sets):
            method_name, method = methods[i % len(methods)]
            numbers = method()
            predictions.append((method_name, numbers))

            print(f"\n[{i+1}번 세트 - {method_name}]")
            print(f"번호: {' '.join([f'{n:2d}' for n in numbers])}")

        print("\n" + "=" * 60)
        return predictions

    def show_statistics(self):
        """통계 정보 표시"""
        print("\n" + "=" * 60)
        print("📊 로또 통계 분석")
        print("=" * 60)

        freq = self.get_frequency_analysis()

        print("\n[TOP 10 자주 나온 번호]")
        for i, (num, count) in enumerate(freq[:10], 1):
            print(f"{i:2d}. 번호 {num:2d}: {count}회 출현")

        print("\n[BOTTOM 10 적게 나온 번호]")
        for i, (num, count) in enumerate(freq[-10:], 1):
            print(f"{i:2d}. 번호 {num:2d}: {count}회 출현")

        # 홀짝 분석
        odd_count = sum(1 for n in self.all_numbers if n % 2 == 1)
        even_count = len(self.all_numbers) - odd_count

        print(f"\n[홀짝 비율]")
        print(f"홀수: {odd_count}회 ({odd_count/len(self.all_numbers)*100:.1f}%)")
        print(f"짝수: {even_count}회 ({even_count/len(self.all_numbers)*100:.1f}%)")

        print("=" * 60 + "\n")


def main():
    """메인 실행 함수"""
    print("""
    ╔═══════════════════════════════════════╗
    ║     🎱 로또 번호 예측기 v1.0 🎱      ║
    ╚═══════════════════════════════════════╝
    """)

    predictor = LottoPredictor()

    # 최근 100회차 데이터 로드 (더 많은 데이터를 원하면 숫자 조정)
    # 전체 데이터를 로드하려면 fetch_lotto_data(1, None) 사용
    latest_round = 1150  # 대략적인 최신 회차
    start_round = max(1, latest_round - 100)

    try:
        predictor.fetch_lotto_data(start_round, latest_round)
    except Exception as e:
        print(f"데이터 로드 실패: {e}")
        print("샘플 데이터로 진행합니다...")
        # 실패시 랜덤 예측만 제공

    # 통계 표시
    if predictor.history:
        predictor.show_statistics()

    # 예측 번호 생성
    num_sets = 5
    print(f"\n{num_sets}개의 번호 세트를 생성합니다...\n")

    predictions = predictor.generate_predictions(num_sets)

    print("\n💡 참고사항:")
    print("- 이 프로그램은 재미와 학습 목적으로 제작되었습니다.")
    print("- 로또는 순수한 확률 게임이며, 예측은 참고용입니다.")
    print("- 행운이 함께 하기를 바랍니다! 🍀")
    print()


if __name__ == "__main__":
    main()
