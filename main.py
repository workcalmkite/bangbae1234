import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="대한민국 축구 선수 정보 앱",
    page_icon="⚽",
    layout="wide"
)

players = [
    {
        "이름": "손흥민",
        "영문명": "Son Heung-min",
        "출생": "1992년",
        "포지션": "공격수",
        "소속팀": "토트넘 홋스퍼",
        "장점": "스피드, 슈팅, 골 결정력",
        "설명": "대한민국 축구 국가대표 주장으로 세계적인 공격수입니다."
    },
    {
        "이름": "김민재",
        "영문명": "Kim Min-jae",
        "출생": "1996년",
        "포지션": "수비수",
        "소속팀": "바이에른 뮌헨",
        "장점": "몸싸움, 수비력, 제공권",
        "설명": "강한 피지컬과 빠른 판단력을 가진 중앙 수비수입니다."
    },
    {
        "이름": "이강인",
        "영문명": "Lee Kang-in",
        "출생": "2001년",
        "포지션": "미드필더",
        "소속팀": "파리 생제르맹",
        "장점": "드리블, 패스, 창의성",
        "설명": "뛰어난 기술과 패스 감각을 가진 미드필더입니다."
    },
    {
        "이름": "황희찬",
        "영문명": "Hwang Hee-chan",
        "출생": "1996년",
        "포지션": "공격수",
        "소속팀": "울버햄프턴",
        "장점": "돌파, 활동량, 압박",
        "설명": "저돌적인 플레이와 빠른 돌파가 강점인 공격수입니다."
    },
    {
        "이름": "조규성",
        "영문명": "Cho Gue-sung",
        "출생": "1998년",
        "포지션": "공격수",
        "소속팀": "미트윌란",
        "장점": "헤딩, 위치 선정, 제공권",
        "설명": "월드컵에서 인상적인 활약을 보여준 스트라이커입니다."
    }
]

df = pd.DataFrame(players)

st.title("⚽ 대한민국 축구 선수 정보 앱")
st.write("선수를 검색하고, 포지션별로 확인하고, 선수 정보를 비교할 수 있는 앱입니다.")

st.divider()

search = st.text_input("🔍 선수 이름 검색", placeholder="예: 손흥민, 김민재, 이강인")

position = st.selectbox(
    "📌 포지션 선택",
    ["전체"] + sorted(df["포지션"].unique().tolist())
)

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["이름"].str.contains(search, case=False) |
        filtered_df["영문명"].str.contains(search, case=False)
    ]

if position != "전체":
    filtered_df = filtered_df[filtered_df["포지션"] == position]

st.subheader("📋 선수 목록")
st.dataframe(filtered_df, use_container_width=True)

st.divider()

st.subheader("⭐ 선수 상세 정보")

if len(filtered_df) > 0:
    selected_player = st.selectbox(
        "자세히 볼 선수를 선택하세요",
        filtered_df["이름"].tolist()
    )

    player = df[df["이름"] == selected_player].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"""
        ### {player['이름']}
        **영문명:** {player['영문명']}  
        **출생:** {player['출생']}  
        **포지션:** {player['포지션']}  
        **소속팀:** {player['소속팀']}
        """)

    with col2:
        st.success(f"""
        ### 장점
        {player['장점']}

        ### 설명
        {player['설명']}
        """)

else:
    st.warning("검색 결과가 없습니다.")

st.divider()

st.subheader("📊 포지션별 선수 수")

position_count = df["포지션"].value_counts()
st.bar_chart(position_count)

st.divider()

st.subheader("📝 나만의 선수 메모장")

memo = st.text_area("선수에 대해 기억하고 싶은 내용을 적어보세요.")

if st.button("메모 확인"):
    if memo.strip():
        st.success("작성한 메모입니다.")
        st.write(memo)
    else:
        st.warning("메모를 입력해 주세요.")

st.divider()

st.caption("Made with Streamlit | 대한민국 축구 선수 정보 앱")
