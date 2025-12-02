import os

message = os.environ.get("GREETING_MESSAGE", "przykładowa wiadmość")

print("--- Skrypt z Env ---")
print(f"{message}")
