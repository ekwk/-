import streamlit as st
import math
import random
import pandas as pd
import os
import base64

# 웹페이지 기본 설정
st.set_page_config(page_title="다기능 계산기 & 시뮬레이터", page_icon="🧮", layout="wide")

# 사이드바 메뉴 구성
st.sidebar.title("📁 메뉴 선택")
app_mode = st.sidebar.radio("원하는 기능을 선택하세요:", ["일반/공학 계산기", "🎲 확률 시뮬레이터", "🐱 oiiai 고양이"])

# --- 1. 일반/공학 계산기 기능 ---
if app_mode == "일반/공학 계산기":
    st.title("🧮 다기능 계산기 웹앱")
    st.write("사칙연산, 모듈러 연산, 지수 연산, 로그 연산을 지원하는 계산기입니다.")
    st.markdown("---")

    operation = st.selectbox(
        "사용할 연산을 선택하세요:",
        ("덧셈 (+)", "뺄셈 (-)", "곱셈 (*)", "나눗셈 (/)", "모듈러 (%)", "지수 (^)", "로그 (log)")
    )

    col1, col2 = st.columns(2)

    with col1:
        if operation == "로그 (log)":
            num1 = st.number_input("밑 (Base)을 입력하세요", value=10.0, step=1.0)
        else:
            num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0, step=1.0)

    with col2:
        if operation == "로그 (log)":
            num2 = st.number_input("진수 (Value)를 입력하세요", value=1.0, step=1.0)
        elif operation == "지수 (^)":
            num2 = st.number_input("지수 (Exponent)를 입력하세요", value=2.0, step=1.0)
        else:
            num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0, step=1.0)

    if st.button("계산하기", type="primary"):
        try:
            if operation == "덧셈 (+)":
                result = num1 + num2
                st.success(f"**결과:** {num1} + {num2} = {result}")
            elif operation == "뺄셈 (-)":
                result = num1 - num2
                st.success(f"**결과:** {num1} - {num2} = {result}")
            elif operation == "곱셈 (*)":
                result = num1 * num2
                st.success(f"**결과:** {num1} * {num2} = {result}")
            elif operation == "나눗셈 (/)":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                else:
                    result = num1 / num2
                    st.success(f"**결과:** {num1} / {num2} = {result}")
            elif operation == "모듈러 (%)":
                if num2 == 0:
                    st.error("0으로 나눌 수 없습니다.")
                else:
                    result = num1 % num2
                    st.success(f"**결과:** {num1} % {num2} = {result}")
            elif operation == "지수 (^)":
                result = math.pow(num1, num2)
                st.success(f"**결과:** {num1} ^ {num2} = {result}")
            elif operation == "로그 (log)":
                if num1 <= 0 or num1 == 1:
                    st.error("로그의 '밑'은 1이 아닌 양수여야 합니다.")
                elif num2 <= 0:
                    st.error("로그의 '진수'는 양수여야 합니다.")
                else:
                    result = math.log(num2, num1)
                    st.success(f"**결과:** log_{num1}({num2}) = {result}")
        except Exception as e:
            st.error(f"계산 중 오류가 발생했습니다: {e}")

# --- 2. 확률 시뮬레이터 기능 ---
elif app_mode == "🎲 확률 시뮬레이터":
    st.title("🎲 확률 시뮬레이터")
    st.write("반복 시뮬레이션을 통해 확률 분포를 시각적으로 확인하고 대수의 법칙을 체험해 보세요.")
    st.markdown("---")

    sim_type = st.selectbox("시뮬레이션할 대상을 선택하세요:", ["주사위 던지기", "동전 던지기"])
    trials = st.number_input("시뮬레이션 반복 횟수를 입력하세요 (최대
