import MeCab
import pandas as pd
import ast
import time


# 시간 측정 데코레이터
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time} seconds.")
        return result
    return wrapper


##############################
# 기능 : text를 토큰화하여 리스트로 반환한다
def tokenize_text(text):
    pos_tags = ['NNG', 'NNP', 'NNB', 'VV', 'VA', 'MM', 'MAG', 'MAJ', 'IC', 'SF', 'SY']

    # 1. mecab 형태소 분석
    tagger = MeCab.Tagger()      # MeCab 객체 생성
    parsed = tagger.parse(text)  # 텍스트 형태소 분석
    lines = parsed.split('\n')  # 결과를 줄 단위로 분리

    # 2. 필요한 품사 태그가 있는 토큰만 추출
    tokens = []
    for line in lines:
        if '\t' in line:
            parts = line.split('\t')
            token = parts[0]
            token_info = parts[1]
            pos_info = token_info.split(',')[0]

            # 합성 품사의 경우 첫 번째 품사 추출
            if '+' in pos_info:
                pos = pos_info.split('+')[0]
            else:
                pos = pos_info

            if pos in pos_tags:
                tokens.append(token)

    # 3. 1글자 토큰 거르기 (!, ? 제외)
    filtered_tokens = [token for token in tokens if len(token) > 1 or token in ['!', '?']]

    return filtered_tokens


###########################
# 기능 : .csv 파일에 토큰화를 적용하여 새로운 파일로 저장한다
@time_decorator
def make_tokenized_csv_file(fpath_to_read, text_column_name, fpath_to_save):
    # 1. 데이터 읽어오기
    print("[progress 1/3] 데이터 읽어오기")
    df = pd.read_csv(fpath_to_read, encoding="utf-8")

    # 2. csv 파일에 spacing 적용시키기
    print("[progress 2/3] csv 파일에 tokenizing 적용시키기")
    df['tokens'] = df[text_column_name].apply(tokenize_text)

    # 3. spacing이 적용된 데이터를 파일로 저장하기
    print("[progress 3/3] tokenizing이 적용된 데이터를 파일로 저장하기")
    df.to_csv(fpath_to_save, encoding='utf-8', index=False)  # csv 파일로 저장

    print("[done]")
