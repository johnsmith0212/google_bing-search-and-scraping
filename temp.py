# initial_text = "ã791-8032æåªçæ¾å±±å¸åæé¢çº704TELï¼089-974-8008FAXï¼089-974-8002愛媛県松山市南斎院町"
# decoded_text = initial_text.encode('latin1', errors='ignore').decode('utf-8', errors='ignore')

# print(decoded_text)


# import re

# pattern = r".*会社$"
# pattern = r"\d{3}-\d{3}-\d{4}"
# text = "899プロコンセ株式会社"
# match = re.match(pattern, text)

# if match:
#     print("マッチしました！")
# else:
#     print("マッチしませんでした。")

import re

def remove_non_japanese(text):
    # 日本語以外の文字を削除
    japanese_text = re.sub(r'[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\s]', '', text)
    
    return japanese_text

# テスト用文字列
text = "Hello こんに ちは 123 ａｂｃ！＠＃"

# 日本語のみを残す
japanese_text = remove_non_japanese(text)

print(japanese_text)