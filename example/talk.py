import voice
import weather
import map
import quiz

def find_address(text):
    index = text.find("날씨")
    address = text[:index]
    return address

def create_weather_text(address):
    coord = map.get_coord_by_address(address)
    if coord == None:
        return "%s을 찾지 못했습니다." % address

    weather_info = weather.get_weather_by_coord(coord[0], coord[1])
    if weather_info != None:
        return "%s의 현재 온도는 %d 도이고, 습도는 %d 퍼센트입니다." % (address, weather_info['main']['temp'], weather_info['main']['humidity'])
    else:
    	return "날씨를 받아오던 중 오류가 발생하였습니다."

def start_quiz():
    quiz_item = quiz.get_random_quiz()
    quiz_answer = quiz_item["answer"]
    quiz_hint = quiz_item["questions"]
    point = 10

    voice.speech("안녕하세요 기가지니 입니다. 지금부터 퀴즈를 시작하겠습니다. 힌트를 듣고 정답을 말해주세요")
    for i in range(len(quiz_hint)):
        voice.speech("%d번 힌트 입니다. %s" % (i + 1, quiz_hint[i]))

        input_text = voice.get_text_from_voice()
        score = quiz.check_answer(quiz_item, input_text)
        if score == 0:
            voice.speech("정답입니다.")
            point_text = "점수는 %d점 입니다." % point
            print(point_text)
            voice.speech(point_text)
            break
        else:
            voice.speech("땡 오답입니다.")
            point = point + score
    else:
        answer_text = "정답은 %s입니다." % quiz_answer
        print(answer_text)
        voice.speech(answer_text)
    voice.speech("퀴즈 게임이 끝났습니다. 감사합니다.")


def main():
    while True:
        if voice.detect_wake_up_word():
            input_text = voice.get_text_from_voice()
            if "날씨" in input_text:
                voice.speech(create_weather_text(find_address(input_text)))
            elif input_text.find("퀴즈") >= 0:
                start_quiz()
            else:
                query_result = voice.query_by_text(input_text)
                voice.speech(query_result)

if __name__ == "__main__":
    main()