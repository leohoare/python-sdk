import typing
from numbers import Number

from src.exception.general_error import GeneralError
from src.exception.open_feature_error import OpenFeatureError
from src.flag_evaluation.error_code import ErrorCode
from src.flag_evaluation.flag_evaluation_details import FlagEvaluationDetails
from src.flag_evaluation.flag_type import FlagType
from src.flag_evaluation.reason import Reason
from src.provider.provider import AbstractProvider


class OpenFeatureClient:
    def __init__(
        self,
        name: str,
        version: str,
        context=None,
        hooks: list = [],
        provider: AbstractProvider = None,
    ):
        self.name = name
        self.version = version
        self.context = context
        self.hooks = hooks
        self.provider = provider

    def get_boolean_value(
        self,
        key: str,
        default_value: bool,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> bool:
        return self.evaluate_flag_details(
            FlagType.BOOLEAN,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        ).value

    def get_boolean_details(
        self,
        key: str,
        default_value: bool,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> FlagEvaluationDetails:
        return self.evaluate_flag_details(
            FlagType.BOOLEAN,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        )

    def get_string_value(
        self,
        key: str,
        default_value: str,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> str:
        return self.evaluate_flag_details(
            FlagType.STRING,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        ).value

    def get_string_details(
        self,
        key: str,
        default_value: str,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> FlagEvaluationDetails:
        return self.evaluate_flag_details(
            FlagType.STRING,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        )

    def get_number_value(
        self,
        key: str,
        default_value: Number,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> Number:
        return self.evaluate_flag_details(
            FlagType.NUMBER,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        ).value

    def get_number_details(
        self,
        key: str,
        default_value: Number,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> FlagEvaluationDetails:
        return self.evaluate_flag_details(
            FlagType.NUMBER,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        )

    def get_object_value(
        self,
        key: str,
        default_value: dict,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> dict:
        return self.evaluate_flag_details(
            FlagType.OBJECT,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        ).value

    def get_object_details(
        self,
        key: str,
        default_value: dict,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> FlagEvaluationDetails:
        return self.evaluate_flag_details(
            FlagType.OBJECT,
            key,
            default_value,
            evaluation_context,
            flag_evaluation_options,
        )

    def evaluate_flag_details(
        self,
        flag_type: FlagType,
        key: str,
        default_value: typing.Any,
        evaluation_context: typing.Any = None,
        flag_evaluation_options: typing.Any = None,
    ) -> FlagEvaluationDetails:
        try:
            if flag_type is FlagType.BOOLEAN:
                return self.provider.get_boolean_details(
                    key,
                    default_value,
                    evaluation_context,
                    flag_evaluation_options,
                )

            elif flag_type is FlagType.NUMBER:
                return self.provider.get_number_details(
                    key,
                    default_value,
                    evaluation_context,
                    flag_evaluation_options,
                )

            elif flag_type is FlagType.OBJECT:
                return self.provider.get_object_details(
                    key,
                    default_value,
                    evaluation_context,
                    flag_evaluation_options,
                )
            # Fallback case is a string object
            elif flag_type is FlagType.OBJECT:
                return self.provider.get_string_details(
                    key,
                    default_value,
                    evaluation_context,
                    flag_evaluation_options,
                )
            else:
                raise GeneralError(error_message="Unknown flag type")

        except OpenFeatureError:
            return FlagEvaluationDetails(
                key=key,
                value=default_value,
                reason=Reason.ERROR,
                error_code=ErrorCode.GENERAL,
            )
