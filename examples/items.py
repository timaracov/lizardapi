from lizardapi import LizardAPI, RouterGroup
from lizardapi.methods import GET, POST, DELETE
from lizardapi.requests import build_request
from lizardapi.responses import JsonResponse
from lizardapi.params import Query, Path
from lizardapi.memtypes import JSON


mem_storage = [
    {"id": 1, "itemName": "book"},
    {"id": 2, "itemName": "coffee"},
    {"id": 3, "itemName": "card"},
    {"id": 4, "itemName": "pen"},
]


@build_request()
class ItemsParams:
    num: int = Query(10, ge=10, lt=100)                 # type:ignore
    page: int = Query(0, ge=0)                          # type:ignore


@build_request(body_content_type=JSON)
class ItemCreate:
    replace_if_exist: bool = Query(False)               # type:ignore
    id: int = 0
    itemName: str = "uknown"


@build_request()
class OneItemParam:
    id: int = Path()                                    # type:ignore


def build_api():
    api = LizardAPI()

    @api.route(GET, "/versions")
    def get_api_versions():
        pass

    item_group = RouterGroup("/items")

    @item_group.route(POST)
    def add_item():
        pass

    @item_group.route(GET)
    def get_items(params: ItemsParams):
        return mem_storage[params.page:params.page+params.num]

    @item_group.route(GET, "/{id}")
    def get_item(param: OneItemParam):
        for item in mem_storage:
            if item["id"] == param.id:
                return JsonResponse(item)
        return JsonResponse({})

    @item_group.route(DELETE, "/{id}")
    def delete_item(param: OneItemParam):
        for ind, item in enumerate(mem_storage.copy()):
            if item["id"] == param.id:
                del mem_storage[ind]
                return JsonResponse({"message": "deleted"})
        return JsonResponse({"message": "deleted"}, 404)

    api.mount_group(item_group)

    return api


if __name__ == "__main__":
    api = build_api()

    api.run(
        host="localhost",
        port=8080,
        workers=1,
        reload=True,
    )
