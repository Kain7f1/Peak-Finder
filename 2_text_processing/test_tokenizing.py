import MeCab
import pandas as pd
from tokenizing_module import tokenize_text, make_tokenized_csv_file

fpath_to_read = "3_spaced_data.csv"
text_column_name = "spaced_text"
fpath_to_save = "5_tokenized_data.csv"

# 토큰화된 파일 만들기
make_tokenized_csv_file(fpath_to_read, text_column_name, fpath_to_save)

#########################################################

text_1 = "생각해보니까"

# [test 1]
# m = MeCab.Tagger()
# parsed = m.parse(text_1)  # text 형태소 분석
# print(parsed)

# [test 2]
# tokens = tokenize_text(text_1)
# print(tokens)

