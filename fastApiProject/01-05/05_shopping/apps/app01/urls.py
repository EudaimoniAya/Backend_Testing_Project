from fastapi import APIRouter

shop = APIRouter()

# 无需写"/shop/food"，因为在include_router中会根据prefix前缀参数创建一个/shop
# 如果参数中添加了，那么这里多写在文档中会重复，如果没添加则这里写"/shop/food"不会重复
@shop.get("/food")
def shop_food():
    return {"shop": "food"}


@shop.get("/bed")
def shop_bed():
    return {"shop": "bed"}