from Models.emso_data_retriever import EMSODataRetriever
import logging


class DataRetrieverCreator:
    def __init__(self, logger):
        self.logger = logger
        self._retrievers = {
            "EMSO": EMSODataRetriever(self.logger)
        }
        self.logger.info("retriever creator done")

    @property
    def keys(self):
        return self._retrievers.keys()

    def get_retriever(self, retriever_type):
        if retriever_type in self._retrievers.keys():
            return self._retrievers[retriever_type]
        else:
            return None
