import streamlit as st
import math

# 웹페이지 기본 설정
st.set_page_config(page_title="다기능 계산기", page_icon="🧮")

st.title("🧮 다기능 계산기 웹앱")
st.write("사칙연산, 모듈러 연산, 지수 연산, 로그 연산을 지원하는 계산기입니다.")
st.markdown("---")

# 연산 종류 선택
operation = st.selectbox(
    "사용할 연산을 선택하세요:",
    ("덧셈 (+)", "뺄셈 (-)", "곱셈 (*)", "나눗셈 (/)", "모듈러 (%)", "지수 (^)", "로그 (log)")
)

# 입력 필드 레이아웃 설정 (2단 분할)
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

# 계산 버튼
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
            # 로그 연산의 예외 처리 (밑은 1이 아닌 양수, 진수는 양수여야 함)
            if num1 <= 0 or num1 == 1:
                st.error("로그의 '밑'은 1이 아닌 양수여야 합니다.")
            elif num2 <= 0:
                st.error("로그의 '진수'는 양수여야 합니다.")
            else:
                result = math.log(num2, num1)
                st.success(f"**결과:** log_{num1}({num2}) = {result}")
                
    except Exception as e:
        st.error(f"계산 중 오류가 발생했습니다: {e}")
