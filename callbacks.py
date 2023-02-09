import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objects as go

from utils import MBTI, random_avatar


def get_callbacks(app):
    @app.callback(
        Output("avatar", "src"),
        Input("avatar-button", "n_clicks"),
    )
    def update_avatar(clicks):
        return random_avatar()

    @app.callback(
        Output("pie-chart", "figure"),
        Input("mbti-input", "value"),
    )
    def update_pie_chart(mbti):
        color = px.colors.diverging.RdBu
        if mbti:        # mbti가 선택이 된 경우
            color = [
                "rgb(178,24,43)" if mbti == m else "#323130"
                for m in MBTI
            ]

        # 파이차트 생성
        pie_chart = go.Figure(
            [
                go.Pie(     # 파이차트 만들기
                    values=[1] * 16,            # 파이차트 16등분
                    labels=MBTI,
                    hole=0.6,                   # 중앙에 구멍이 뚫림
                    textinfo="label",
                    marker=dict(colors=color),  # 각 구간의 색 지정
                    hoverinfo="label",          # 마우스를 올렸을 때 나오는 값
                    textfont=dict(size=20),     # 글씨체 변경
                )
            ]
        )

        pie_chart.update_layout(    # 파이차트의 레이아웃 설정
            margin=dict(t=0, l=0, r=0, b=0),    # 마진 설정
            paper_bgcolor="#323130",            # 파이차트의 배경 색
            plot_bgcolor="#323130",
            showlegend=False,                   # 범례(legend) 삭제
        )
        return pie_chart    # 함수에서 리턴을 해주어야 화면에 들어감

    @app.callback(
        Output("name", "children"),
        Input("name-input", "value"),
    )
    def update_name(name):
        return f"이름: {name}" if name else "이름: "

    @app.callback(
        Output("age", "children"),
        Input("age-input", "value"),
    )
    def update_age(age):
        if age is None:
            return "나이"
        return f"나이 {age}"
        # return f"나이: {age}" if age else "나이: "

    @app.callback(
        Output("mbti-input", "value"),
        Input("pie-chart", "clickData"),
    )
    # 파이차트에서 항목 선택 시 mbti 입력 레이블 변경
    def update_mbti_input_from_pie_chart(mbti):
        if mbti:    # mbti 선택 값이 none인 경우는 제외
            return mbti["points"][0]["label"]
        return None
