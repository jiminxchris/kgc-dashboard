import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(
    page_title="KGC Brand Strategy - Weekly Insight",
    page_icon="🔴",
    layout="wide"
)

# 커스텀 CSS (KGC 브랜드 느낌의 Red 포인트)
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1, h2, h3 { color: #b41e2d; }
    </style>
    """, unsafe_allow_html=True)

# 2. 헤더 섹션
st.title("🔴 주간 마케팅 통찰 보고서")
st.subheader("정관장 에브리타임 밸런스 (리뉴얼) | 2026년 3월 4주차")
st.divider()

# 3. 핵심 KPI 지표 (Metric)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="수도권 판매량 (편의점)", value="+15%", delta="전주 대비", delta_color="normal")
with col2:
    st.metric(label="지방 판매량 (대형마트)", value="-2%", delta="-2.0", delta_color="inverse")
with col3:
    st.metric(label="2030 사회초년생 비중", value="45%", delta="핵심 타겟 유입")
with col4:
    st.metric(label="아웃도어 키워드 언급", value="+30%", delta="등산·테니스")

st.write("")

# 4. 판매 실적 및 타겟 분석 (Charts)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("### 📊 지역별 판매 증감 추이")
    sales_data = pd.DataFrame({
        'Region': ['수도권 (편의점)', '지방 (대형마트)'],
        'Growth': [15, -2]
    })
    fig_sales = px.bar(sales_data, x='Region', y='Growth', 
                       color='Growth', color_continuous_scale=['#b41e2d', '#e0e0e0', '#2e7d32'],
                       text_auto='.1f')
    fig_sales.update_layout(showlegend=False, height=350)
    st.plotly_chart(fig_sales, use_container_width=True)

with chart_col2:
    st.markdown("### 👥 구매 고객 연령층 분포")
    age_data = pd.DataFrame({
        'Age': ['2030 사회초년생', '4050 세대', '기타'],
        'Value': [45, 40, 15]
    })
    fig_age = px.pie(age_data, values='Value', names='Age', 
                     color_discrete_sequence=['#b41e2d', '#6d0f18', '#cccccc'],
                     hole=0.4)
    fig_age.update_layout(height=350)
    st.plotly_chart(fig_age, use_container_width=True)

# 5. 고객 리뷰 및 특이사항 (VOC)
st.divider()
voc_col1, voc_col2 = st.columns(2)

with voc_col1:
    st.markdown("### ✅ 고객 긍정 리뷰 (Positive)")
    st.success("**'선물용으로 적합한 세련된 패키징'**")
    st.success("**'리뉴얼 후 부드러워진 목넘김(쓴맛 완화)'**")

with voc_col2:
    st.markdown("### ⚠️ 개선 필요 사항 (Negative)")
    st.warning("**'가격 인상에 대한 심리적 저항감 발생'**")
    st.error("**'패키지 개봉 시 뻑뻑함 이슈 (QA 확인 필요)'**")

# 6. 전략적 제언 (Strategic Suggestions)
st.info("💡 **팀장 제언:** '등산/테니스' 키워드 급증에 따라, 주말 아웃도어 거점(북한산, 테니스장 인근 편의점) 대상 샘플링 프로모션 강화를 제안함.")

# 푸터
st.caption(f"본 보고서는 KGC 브랜드 전략실 내부용 자료입니다. | 담당자: 팀장 Chris Lin")
