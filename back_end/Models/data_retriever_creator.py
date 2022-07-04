from Models.emso_data_retriever import EMSODataRetriever


class DataRetrieverCreator:
    def __init__(self):
        self._classes = {
            "EMSO": EMSODataRetriever
        }

    @property
    def keys(self):
        return self._classes.keys()

    def get_retriever(self, retriever_type):
        if retriever_type in self._classes.keys():
            return self._classes[retriever_type]()
        else:
            return None
