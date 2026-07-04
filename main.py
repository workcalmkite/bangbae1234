import streamlit as st

st.set_page_config(
    page_title="대한민국 축구 선수 소개",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ 대한민국 축구 선수 소개")
st.write("대한민국을 대표하는 축구 선수들을 소개합니다!")

st.divider()

# 손흥민
st.header("🇰🇷 손흥민 (Son Heung-min)")
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/8/8d/Son_Heung-min_2022.jpg",
        width=250
    )

with col2:
    st.write("""
**출생:** 1992년 7월 8일

**포지션:** 공격수

**소속:** 토트넘 홋스퍼

**등번호:** 7번

손흥민 선수는 대한민국 축구 국가대표 주장으로,
빠른 스피드와 뛰어난 골 결정력을 가진 세계적인 축구 선수입니다.
프리미어리그 득점왕을 차지한 최초의 아시아 선수입니다.
""")

st.divider()

# 김민재
st.header("🇰🇷 김민재 (Kim Min-jae)")
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/7/76/Kim_Min-jae_2023.jpg",
        width=250
    )

with col2:
    st.write("""
**출생:** 1996년 11월 15일

**포지션:** 수비수

**소속:** 바이에른 뮌헨

김민재 선수는 강한 몸싸움과 뛰어난 수비 능력을 가진
대한민국 최고의 중앙 수비수입니다.
""")

st.divider()

# 이강인
st.header("🇰🇷 이강인 (Lee Kang-in)")
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/2/2b/Lee_Kang-in_2023.jpg",
        width=250
    )

with col2:
    st.write("""
**출생:** 2001년 2월 19일

**포지션:** 미드필더

**소속:** 파리 생제르맹(PSG)

이강인 선수는 뛰어난 드리블과 패스 능력을 가진
대한민국 대표 미드필더입니다.
""")

st.divider()

st.subheader("🏆 대한민국 축구의 자랑")

st.success("""
대한민국 축구는 월드컵과 아시안컵 등 다양한 국제대회에서
멋진 활약을 펼치고 있으며,
손흥민, 김민재, 이강인 선수는 세계 최고의 리그에서 활약하는
대한민국의 자랑스러운 축구 선수들입니다.
""")

st.balloons()
