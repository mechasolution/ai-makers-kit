import voice
import paho.mqtt.client as mqtt

broker_address = "xxx.xxx.xxx.xxx" #브로커의 IP를 입력합니다.

# get_target_status()에서 리턴된 값을 토픽에 발행해주는 함수
def publish_target_status(target_status):
  # 리턴된 값에 HIGH 또는 LOW가 없다면 False를 리턴합니다.
  if target_status != "HIGH" and target_status != "LOW":
    return False
  client1 = mqtt.Client() # Mqtt라이브러리의 Client 인스턴스를 생성합니다.
  client1.connect(broker_address, 1883) # connect()메서드를 사용해서 브로커에 연결해줍니다.
  # NodeMCU에서 구독하고 있는 AMk/Control/node1에 처리된 데이터를 발행합니다.
  client1.publish("AMK/Control/node1", target_status)
  # 발행처리가 완료되면 브로커와 연결을 끊어줍니다.
  client1.disconnect()
  # 모든 과정이 끝나면 True를 리턴합니다.
  return True

# TTS로 받아온 음성인식 텍스트에서 켜줘와 꺼줘를 구분해주는 함수
def get_target_status(input_text):
  if(input_text.find("조명 켜줘") != -1): #켜줘로 인식되면 HIGH를 리턴합니다.
    print("켜줘를 인식했습니다.")
    return "HIGH"
  elif(input_text.find("조명 꺼줘") != -1): #꺼줘로 인식되면 LOW를 리턴합니다.
    print("꺼줘를 인식헸습니다.")
    return "LOW"
  else: # 입력된 텍스트에 명령이 없다면 None을 리턴합니다.
    print("잘못된 명령입니다.")
    return None

def main() :
  voice.speech("조명을 제어합니다. 켜줘 또는 꺼줘로 제어해보세요")
  input_text = voice.get_text_from_voice() # TTS를 실행하여 텍스트를 받아옵니다.
  result_target = get_target_status(input_text) # 입력된 텍스트를 입력해 명령을 구분합니다.
  # 구분된 명령을 발행하고 결과를 받아옵니다.
  publish_result = publish_target_status(result_target)

  # 구분된 명령과 발행된 결과값을 처리하여 음성으로 출력합니다.
  if publish_result == True:
    if result_target == "HIGH":
      voice.speech("조명을 켭니다.")
    elif result_target == "LOW":
      voice.speech("조명을 끕니다.")
  else:
    voice.speech("잘못된 명령이 인식되었습니다.")


if __name__ == "__main__" :
  main()
