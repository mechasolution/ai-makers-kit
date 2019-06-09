import paho.mqtt.client as mqtt
import time
import voice
broker_address="192.168.30.65"

recv_message = None
# subscriber 콜백함수
def on_message( client , userdata , message ):
	global recv_message # 전역변수를 가져옵니다.
	# 콜백함수에 들어오는 데이터를 변환하여 변수에 저장하고 토픽과 메세지를 출력합니다.
	recv_message = str(message.payload.decode("utf-8"))
	print(recv_message)
	print("message topic=",message.topic)

def subscribe_message():
	client1 = mqtt.Client() # mqtt Client 인스턴스를 생성합니다.
	client1.connect(broker_address, 1883) # 브로커에 연결합니다.
	client1.on_message = on_message # 콜백함수를 설정해줍니다.
	client1.subscribe("AMK/Sensor/node1") # 원하는 토픽을 구독해줍니다.
	print("Topic Subscribe")
	client1.loop_start() # 구독한 토픽에서 데이터를 받기 위해서 무한루프를 시작합니다.
	global recv_message # 전역변수를 가져옵니다.

	# 콜백함수에서 메세지가 발행될 때까지 대기하며
	# 메세지가 들어오거나 time_out_value 가 10 이되면 다음코드를 실행합니다.
	time_out_value = 0
	return_message = ""
	while recv_message == None and time_out_value < 11:
		print("waiting... %d"%time_out_value)
		time_out_value += 1
		time.sleep(1)
	# 조건문을 사용해 결과에 따라 출력해줍니다.
	if recv_message == None:
		print("센서 값을 수신할 수 없습니다.")
		return_message = "센서 값을 수신할 수 없습니다."
	else:
		print("입력된 센서 값은 %s 입니다."%recv_message)
		return_message = "입력된 센서 값은 %s 입니다."%recv_message
	recv_message = None # 변수를 초기화 합니다. client1.loop_stop()
	client1.disconnect() # 클라이언트를 종료합니다.
	return return_message # 결과를 리턴해줍니다.

def main():
	voice.speech("연결된 센서의 측정 값을 알려드리겠습니다.")
	result_message = subscribe_message()
	voice.speech(result_message)

if __name__ == "__main__":
	main()