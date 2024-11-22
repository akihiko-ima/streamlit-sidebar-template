from dataclasses import dataclass
from typing import Dict, Callable

# import your streamlit page
from views import first_page, second_page, third_page


@dataclass
class RouterMapping:
    routing_name: str
    icon: str
    streamlit_page: Callable[[], None]


# router mapping
"""
・If you have any pages you would like to route, please add them here.
・The icons in the sidebar use "Google Fonts."
 [https://fonts.google.com/icons](https://fonts.google.com/icons)
"""
routers: Dict[str, RouterMapping] = {
    "router_1": RouterMapping(routing_name="first", icon="home", streamlit_page=first_page),
    "router_2": RouterMapping(routing_name="second", icon="rocket_launch", streamlit_page=second_page),
    "router_3": RouterMapping(routing_name="third", icon="login", streamlit_page=third_page),
}
