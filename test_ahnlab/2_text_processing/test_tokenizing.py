import MeCab
import pandas as pd
from tokenizing_module import tokenize_text, make_tokenized_csv_file

fpath_to_read = "2_spaced_annlab_text.csv"
text_column_name = "spaced_text"
fpath_to_save = "4_tokenized_annlab_text.csv"

# 토큰화된 파일 만들기
make_tokenized_csv_file(fpath_to_read, text_column_name, fpath_to_save)

#########################################################

text_1 = "제이피모건 채이스 어떰? 안랩 가지고 장난친애들이 애네던가? 주식쭉쭉 빠지고 배당율 많이 좋아지면 배당셔틀 시키게 지켜보고 있는데 리츠주들 좋은가격대 놓쳐서애라도 보는중"
text_2 = "안철수 국무총리해서 주신백지신탁하네 안랩 우에댈라나더 떨어질까?"
text_3 = "국장이 털어먹기 좋긴함 ㅋㅋ 호재있을떄 양봉좀 세워주면 개미들이 미친듯이 달려들거든"
text_4 = "안랩 못사서 벼락자지됐지만 안철수가 답이다 그리고 슨피는 신이지 오늘 더 넣을거야 씨발들아!"
text_5 = "퍼포먼스식 https open 카카오 com o gu p jld pw 카카오는 영어로 카카오 치세요 주선 전문 트레이더들이 모여있는 방입니다 주선 잘하시는듯한데 와서 정보 교환해요"
text_6 = "ㅠㅠ 간철수는 대통령 될생각 없다는걸 인증한거지 당대표 떨어지고 나서"
text_7 = "주식으로 선거때마다 한탕 해처먹는 간잽이진짜 확망했으면"
text_8 = "문재앙 난장 년 김기현 vs 안철수의 행보 직격 비교! 김기현은 행정과 의정을 두루 거치면서 문재앙의 선거개입 탄압에도 당당히 투쟁해 화려하게 부활함! "

# [test 1]
m = MeCab.Tagger()
parsed = m.parse(text_4)  # text 형태소 분석
# print(parsed)

# [test 2]
# tokens = tokenize_text(text_6)
# print(tokens)
