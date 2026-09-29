"""咖啡烘焙核心逻辑：生豆、烘焙机、质检和计费。"""

import json


def new_game():
    return {"batches": {}, "roaster_load": 0, "roaster_capacity": 2, "beans": 100, "quality": 100, "day": 1, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def register(state, batch_id, amount):
    state["batches"][batch_id] = {"amount": amount}
    state["beans"] -= amount
    return True


def roast(state, batch_id):
    state["roaster_load"] += 1
    return True


def fee(state, batch_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, batch_id, amount):
    return True


def produce(state, amount):
    return True


def color_event(state):
    state["quality"] -= 10
    state["quality"] -= 10
    return state["quality"]


def cool(state, batch_id):
    return True


def main():
    print("咖啡烘焙 - 命令: register/roast/fee/cancel/produce/color/cool/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
