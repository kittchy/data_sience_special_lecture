import json
import codecs
import sentencepiece as spm


# load JSON 20newsgroup data
with open("newsgroups.json") as fd:
    data = json.load(fd)
# content, target(=class ID), target_name(=newsgroup name)
content = data["content"]
target = data["target"]
target_names = data["target_names"]
# get dictionary values for content, target, and target_names
content_value = content.values()
target_value = target.values()
target_name_value = target_names.values()
# extract lists for content, target, and target_names
content_value_list = list(content_value)  # メッセージテキスト本体
target_value_list = list(target_value)  # メッセージのカテゴリ ID
target_namevalue_list = list(target_name_value)
num_docs = 11314  # (=len(content.keys())


print(*content_value_list, sep="\n", file=codecs.open("content.txt", "w", "utf-8"))
