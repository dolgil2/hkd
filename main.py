import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="시티큐브 매출 대시보드", page_icon="📊", layout="wide")

st.title("📊 시티큐브 매출 분석 대시보드")
st.markdown("---")

# 사이드바
st.sidebar.title("🎛️ 필터 옵션")
st.sidebar.selectbox("기간 선택", ["전체", "2024년", "2025년"])
st.sidebar.multiselect("담당자 선택", ["손승주", "원종윤", "김경호"])

# 메인 콘텐츠
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("총 매출", "15.2억원", "12.3%")
with col2:
    st.metric("활성 캠페인", "10개", "2개")
with col3:
    st.metric("총 매체", "162기", "5기")
with col4:
    st.metric("월 평균", "1.5억원", "8.7%")

st.markdown("---")
st.info("🚀 개발 중인 대시보드입니다. 단계별로 기능이 추가될 예정입니다.")
