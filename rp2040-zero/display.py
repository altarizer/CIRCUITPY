import time
import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP4)  # 버튼 핀 설정
btn.direction = Direction.INPUT
btn.pull = Pull.UP
"""
try:
    i2c.deinit()
except NameError:
    print("I2C가 아직 생성되지 않았습니다.")
"""
try:
    
    # I2C 객체가 생성되지 않았을 경우에만 생성합니다.
    if not hasattr(board, 'I2C'):
        i2c = busio.I2C(scl=board.GP3, sda=board.GP2)  # I2C 설정
    else:
        i2c = board.I2C()  # 이미 존재하는 경우 I2C 객체를 사용
    

    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # 디스플레이 주소 설정

    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
    splash = displayio.Group()
    display.root_group = splash

    color_bitmap = displayio.Bitmap(128, 32, 1)  # 전체 화면 검은색
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x000000  # 검은색

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    start_time = None  # start_time을 None으로 초기화
    elapsed_time = 0  # 초기 경과 시간 설정
    previous_elapsed_time = 0  # 경과 시간 멈추기 전 마지막 시간 저장
    
    long_press_time = 2  # long press를 2초 이상으로 설정
    button_press_time = 0  # 버튼 눌린 시간
    
    text_area = label.Label(terminalio.FONT, text="00:00:00", color=0xffffff, x=12, y=20, scale=2)
    splash.append(text_area)

    downCounter = 0
    run = True  # 시간 흐름 제어
    
    while True:
        
        # 버튼 상태 체크
        if not btn.value:  # 버튼이 눌렸을 때
            if button_press_time == 0:  # 버튼이 처음 눌린 순간
                button_press_time = time.monotonic()  # 버튼 눌린 시간 기록
            
            press_duration = time.monotonic() - button_press_time 
            if press_duration >= long_press_time:  # long press로 처리
                print("Long press detected!")
                start_time = None  # 롱프레스 시 시간 초기화
                elapsed_time = 0  # 경과 시간 초기화
                previous_elapsed_time = 0  # 경과 시간 초기화
                
        else:  # 버튼이 떼어졌을 때
            if button_press_time != 0:  # 버튼이 눌려 있었을 때만 동작
                press_duration = time.monotonic() - button_press_time  # 버튼이 눌린 시간 계산
                if press_duration >= long_press_time:  # long press로 처리
                    print("Long press detected!")
                    start_time = None  # 롱프레스 시 시간 초기화
                    elapsed_time = 0  # 경과 시간 초기화
                    previous_elapsed_time = 0  # 경과 시간 초기화
                else:  # short press로 처리
                    print("Short press detected!")
                    run = not run  # run 상태 토글 (True/False)
                    if run:  # run이 True로 변경되면 시간 계산을 시작
                        # 이전에 멈춘 시간을 반영하여 다시 시작
                        start_time = time.monotonic() - previous_elapsed_time
                    else:  # run이 False이면 시간 멈추기
                        previous_elapsed_time = elapsed_time  # 멈춘 시간을 저장
              
              
                button_press_time = 0  # 버튼 눌린 시간 초기화

        if run:  # run이 True일 때만 시간 계산
            if start_time is None:
                start_time = time.monotonic() - previous_elapsed_time  # 이전의 경과 시간을 고려하여 시작
            elapsed_time = time.monotonic() - start_time
        else:
            previous_elapsed_time = elapsed_time  # 시간 멈출 때 경과 시간 저장

        # 경과 시간을 시간, 분, 초로 변환
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        # 형식에 맞게 출력
        formatted_time = f"{hours:03}:{minutes:02}:{seconds:02}"

        # 텍스트를 갱신합니다.
        text_area.text = formatted_time  # 기존 text_area를 갱신
        time.sleep(0.1)  # 100ms마다 상태를 체크

except Exception as e:
    print(f"예외 발생: {e}")
    import microcontroller
    microcontroller.reset()
