import eel
from mymodule import calc

def close_window(closed_page, remained_list):
    print("remained_list", remained_list)

host="localhost"
port=8000

print(f"you can access http://{host}:{port}/main.html")

eel.init("web")
eel.start(
    "main.html",
    mode=None,
    host=host,
    port=port,
    close_callback=close_window,
)
