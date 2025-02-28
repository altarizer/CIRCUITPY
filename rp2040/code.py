import board, busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()
root_group = displayio.Group()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr=True)

bitmaps = [
    displayio.OnDiskBitmap("/0.bmp"),
    displayio.OnDiskBitmap("/1.bmp"),
    displayio.OnDiskBitmap("/2.bmp"),
    displayio.OnDiskBitmap("/3.bmp"),
    displayio.OnDiskBitmap("/4.bmp"),
]

group = displayio.Group()
display.root_group = group

# 첫 번째 이미지 추가
tile_grid = displayio.TileGrid(bitmaps[0], pixel_shader=bitmaps[0].pixel_shader)
group.append(tile_grid)

while True:
    try:
        for i, bitmap in enumerate(bitmaps):
            new_tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
            group[0] = new_tile_grid  # 기존 객체를 교체하여 메모리 누수 방지
            sleep(2 if i == 0 else 1)  # 첫 번째 이미지는 2초, 나머지는 1초 대기
        
    except MemoryError:
        print("메모리 오류 발생! 루프를 계속 실행합니다.")
        sleep(1)  # 약간의 대기 시간을 둬서 메모리 회복 시간 제공
        continue
    
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
        sleep(1)  # 오류 발생 시에도 루프를 유지
        continue
