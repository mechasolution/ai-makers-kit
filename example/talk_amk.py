import voice
import ex3_4_quiz_game as quiz_game
import ex3_5_timer as timer
import ex4_1_get_weather as weather
import ex4_2_dictionary as dictionary
import ex5_1_digitalControl as control
import ex5_2_iot_sensor as sensor

def main():
    while True:
        if voice.detect_wake_up_word():
            input_text = voice.get_text_from_voice()
            print(input_text)
            if input_text.find("퀴즈 게임 시작해 줘") != -1:
                    quiz_game.main()
            elif input_text.find("타이머 시작해 줘") != -1:
                    timer.main()
            elif input_text.find("날씨 알려줘") != -1:
                    weather.main()
            elif input_text.find("사전 시작해 줘") != -1:
                    dictionary.main()
            elif input_text.find("외부 제어 시작해 줘") != -1:
                    control.main()
            elif input_text.find("외부 센서 실행해 줘") != -1:
                    sensor.main()
            else:
                result_answer = voice.query_by_text(input_text)
                voice.speech(result_answer)
if __name__ == "__main__":
    main()