from config import routers


# roting nameとstreamlit_page関数の辞書を作成
router_mappings = {}
for _, router in routers.items():
    router_mappings[router.routing_name] = router.streamlit_page
