# @app.get("/items/{item_id")
# def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/")
# def root():
#     return {"message": "Hello World"}
#
# #path parameters
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id, "name": "John Doe"}
#
# #Query Parameters
# @app.get("/items/")
# def get_items(skip: int = 0, limit: int = 10):
#     return{"skip": skip, "limit": limit}