import typing
from abc import abstractmethod
from numbers import Number


class AbstractProvider:
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_boolean_details(
        self,
        key: str,
        default_value: bool,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ):
        pass

    @abstractmethod
    def get_string_details(
        self,
        key: str,
        default_value: str,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ):
        pass

    @abstractmethod
    def get_number_details(
        self,
        key: str,
        default_value: Number,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ):
        pass

    @abstractmethod
    def get_object_details(
        self,
        key: str,
        default_value: dict,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ):
        pass
