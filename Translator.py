from translate import Translator
translator = Translator(to_lang="ja")


with open('/Users/jeremyantoniani/PycharmProjects/modules/venv/Translator_Test.txt', mode='r') as my_file:
    translation = translator.translate(my_file.read())
    print(translation)
    with open('./Translator_Test-ja.txt', mode='w') as my_file2:
        my_file2.write(translation)



