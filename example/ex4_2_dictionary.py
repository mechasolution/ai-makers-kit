import requests
from bs4 import BeautifulSoup
import voice

def searchKorean(keyword):
    url = "https://stdict.korean.go.kr/search/searchResult.do?searchKeyword=%s"
    response = requests.get(url % keyword)

    if response.status_code == 200:
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        dataLines = bs.select('form#searchDataVO > div.container > ul.result> li > dl > dt > span > font.dataLine')
        meanings = []
        for data in dataLines:
            meanings.append(data.text)
        return meanings
    else:
        return None

def main():
    voice.speech('궁금하신 단어가 무엇인가요?')
    word = voice.get_text_from_voice()
    meanings = searchKorean(word)

    if meanings == None or len(meanings) == 0:
        voice.speech('%s에 관한 뜻을 찾지 못했어요.' % word)
    else:
        voice.speech('사전에서 찾은 검색결과입니다. %s' % meanings[0])


if __name__ == "__main__":
    main()