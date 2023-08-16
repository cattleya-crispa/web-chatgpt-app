from urls import app
import uvicorn
 
if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可
    print("start urls => controller")
    uvicorn.run(app=app)

# port change
#  uvicorn.run(app=app, port=8888)