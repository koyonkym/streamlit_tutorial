import streamlit as st

class MyResource:
    def __init__(self, api_url: str):
        self._url = api_url

    @staticmethod
    @st.cache_resource(ttl=300)
    def get_resource_manager(api_url: str):
        return MyResource(api_url)

# This is cached until Session State is cleared or 5 minutes has elapsed.
resource_manager = MyResource.get_resource_manager("http://example.com/api/")