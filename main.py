from fastapi import FastAPI

app = FastAPI(title="Trading App")

fake_users = [
    {"id": 1, "role": "admin", "name": "bob"},
    {"id": 2, "role": "investor", "name": "john"},
    {"id": 3, "role": "debil", "name": "maga"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user_id == user.get("id")]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "bob"},
    {"id": 2, "role": "investor", "name": "john"},
    {"id": 3, "role": "debil", "name": "maga"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):

    current_user = list(filter(
        lambda user: user.get("id") == user_id,
        fake_users2))[0]

    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
