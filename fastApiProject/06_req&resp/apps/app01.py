from fastapi import APIRouter

app1 = APIRouter()


# 如果路径中有参数，那么下面函数就要有一个同名的参数
@app1.get("/user/1")
def get_user():
    return {
        'user_id': 'root user'
    }


# 而且如果变量中如果取到了某个值，使得路径成为一个已有对应路由的静态路径
# 那么结合路径查找的机制：从程序内从上往下依次查询，如果这个静态路径在前，那么就会执行静态的
# 比如该接口如果传入user_id为1的话，就会执行另一个方法，返回的就不是user_id，而是root user
# 但是如果把这两个接口的顺序调换，那么root user将永远不会被输出，但一般不会这么做，一般会让给定的静态路由放到最前面
@app1.get("/user/{user_id}")
def get_user(user_id: int):
    print("user_id", user_id, type(user_id))
    return {
        'user_id': user_id
    }


@app1.get("/articles/{articles_id}")
def get_user(articles_id: int):
    print("articles_id", articles_id, type(articles_id))
    return {
        'articles_id': articles_id
    }
