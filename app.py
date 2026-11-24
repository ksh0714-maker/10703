import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 눌러 오늘 먹을 맛있는 점심 메뉴를 골라보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "국밥",
    "파스타",
    "햄버거",
    "쌀국수",
    "마라탕",
    "비빔밥",
    "칼국수",
    "샌드위치",
]

# 추천 버튼 생성
if st.button("🎲 점심 메뉴 추천받기", type="primary"):
    # 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(lunch_menus)

    # 결과 출력 및 풍선 애니메이션 효과
    st.balloons()
    st.success(f"오늘의 추천 메뉴는 **{selected_menu}** 입니다! 맛있게 드세요! 😋")
