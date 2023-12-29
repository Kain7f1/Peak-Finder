import MeCab
import pandas as pd
from tokenizing_module import tokenize_text, make_tokenized_csv_file

fpath_to_read = "3_spaced_ecopro_text.csv"
text_column_name = "spaced_text"
fpath_to_save = "5_tokenized_ecopro_text.csv"

# 토큰화된 파일 만들기
make_tokenized_csv_file(fpath_to_read, text_column_name, fpath_to_save)

#########################################################

text_1 = "에코프로 매수를 독려해야함 전국민 자체적 자산증발을 위해 국장 바카라 주식매수를 권장하고복권 구매를 장려해야 한다 풀린돈이 많으니 멍청한놈들 돈을"

# [test 1]
m = MeCab.Tagger()
parsed = m.parse(text_1)  # text 형태소 분석
# print(parsed)

# [test 2]
# tokens = tokenize_text(text_1)
# print(tokens)

