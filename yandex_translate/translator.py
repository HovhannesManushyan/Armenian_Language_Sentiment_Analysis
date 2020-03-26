import requests
import os


# a function which using API get a translated text from a particular language
def get_translation(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20200324T195751Z.d9dfb05b7ca74e4e.67479bad9a2c0fdead2e7d7edddad2146608e908'
    TEXT = text
    LANG = lang
    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return eval(r.text)


# a function that reads the original texts from given files and write the translation in another file
def translator(type_):
    if (type_ == 'Positive'):
        input_folder = 'pos'
        output_file = 'outputPOS.txt'
    if (type_ == 'Negative'):
        input_folder = 'neg'
        output_file = 'outputNEG.txt'
    with open(output_file, 'w', encoding='utf-8') as fw:
        for current_name in os.listdir("aclImdb/test/" + input_folder + "/"):
            current_filename = "aclImdb/test/" + input_folder + "/" + current_name
            with open(current_filename, 'r', encoding='utf-8') as fr:
                text = str(get_translation(fr.read(), 'hy')['text'][0])
                fw.write(text + '\n')


translator('Positive')
translator('Negative')