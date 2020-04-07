import asyncio
import websockets
import pyautogui as pg
import ctypes

PORT = 8000

async def listen(websocket, path):
    while True:
        msg = await websocket.recv()
        print(f"< {msg}")

        greeting = f"ok {msg}!"

        await websocket.send(greeting)
        if msg == 'ml':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x - 10, pos.y)
        elif msg == 'mr':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x + 10, pos.y)
        elif msg == 'up':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x, pos.y - 10)
        elif msg == 'dw':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x, pos.y + 10)
        elif msg == 'ul':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x - 10, pos.y - 10)
        elif msg == 'ur':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x + 10, pos.y - 10)
        elif msg == 'dl':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x - 10, pos.y + 10)
        elif msg == 'dr':
            pos = pg.position()
            ctypes.windll.user32.SetCursorPos(pos.x + 10, pos.y + 10)
        elif msg == 'lc':
            pg.click()
        elif msg == 'rc':
            pg.rightClick()
        elif msg.startswith('typ:'):
            pg.typewrite(msg[4:])
        elif msg.startswith('bs:'):
            pg.hotkey('backspace')
        elif msg.startswith('screen:'):
            pg.screenshot('public\\s.png')
        print(f"> {greeting}")

start_server = websockets.serve(listen, "192.168.2.131", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()