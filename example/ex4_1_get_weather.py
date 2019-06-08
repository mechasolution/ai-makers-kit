import voice
import weather
import map

def create_weather_text(address):
    coord = map.get_coord_by_address(address)
    if coord == None:
        return "%s을 찾지 못했습니다." % address

    weather_info = weather.get_weather_by_coord(coord[0], coord[1])
    if weather_info != None:
        return "%s의 현재 온도는 %d 도이고, 습도는 %d 퍼센트입니다." % (address, weather_info['main']['temp'], weather_info['main']['humidity'])
    else:
    	return "날씨를 받아오던 중 오류가 발생하였습니다."

def main():
    if voice.detect_wake_up_word():
        text = voice.get_text_from_voice()
        if "날씨" in text:
            index = text.find("날씨")
            address = text[:index]
            voice.get_voice_and_speech(create_weather_text(address))

if __name__ == "__main__":
    main()
    