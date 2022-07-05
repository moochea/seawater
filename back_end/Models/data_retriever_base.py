from abc import ABC, abstractmethod


class DataRetrieverBase(ABC):
    '''
    Adaptor for access to each data source.
    '''

    @abstractmethod
    def get_records(self, reference, args_dict={}):
        '''
        Implement the API call to retrieve the various data components.
        Return an instance of the Dataset class.
        :param reference:
        :param args_dict:
        :return: Dataset
        '''
        pass

