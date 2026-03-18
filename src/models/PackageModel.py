from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config

class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"



class OutputText(Output):
    name: Literal["outputText"] = "outputText"
    value: Optional[str]
    type: Literal["string"] = "string"

    class Config:
        title = "Output"

class OutputClasses(Output):
    name: Literal["outputClasses"] = "outputClasses"
    value: Union[dict, list, str, List[dict]]
    type: str = "object"

    @validator("type", always=True)
    def set_type_based_on_value(cls, val, values):
        val = values.get("value")
        if isinstance(val, list):
            return "list"
        return "object"

    class Config:
        title = "Classes"



class OptionModelGpt54(Config):
    name: Literal["gpt-5.4"] = "gpt-5.4"
    value: Literal["gpt-5.4"] = "gpt-5.4"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5.4"

class OptionModelGpt52(Config):
    name: Literal["gpt-5.2"] = "gpt-5.2"
    value: Literal["gpt-5.2"] = "gpt-5.2"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5.2"

class OptionModelGpt51(Config):
    name: Literal["gpt-5.1"] = "gpt-5.1"
    value: Literal["gpt-5.1"] = "gpt-5.1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5.1"

class OptionModelGpt5(Config):
    name: Literal["gpt-5"] = "gpt-5"
    value: Literal["gpt-5"] = "gpt-5"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5"

class OptionModelGpt5Mini(Config):
    name: Literal["gpt-5-mini"] = "gpt-5-mini"
    value: Literal["gpt-5-mini"] = "gpt-5-mini"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5-mini"

class OptionModelGpt5Nano(Config):
    name: Literal["gpt-5-nano"] = "gpt-5-nano"
    value: Literal["gpt-5-nano"] = "gpt-5-nano"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-5-nano"

class OptionModelGpt41(Config):
    name: Literal["gpt-4.1"] = "gpt-4.1"
    value: Literal["gpt-4.1"] = "gpt-4.1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-4.1"

class OptionModelGpt41Mini(Config):
    name: Literal["gpt-4.1-mini"] = "gpt-4.1-mini"
    value: Literal["gpt-4.1-mini"] = "gpt-4.1-mini"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-4.1-mini"

class OptionModelGpt41Nano(Config):
    name: Literal["gpt-4.1-nano"] = "gpt-4.1-nano"
    value: Literal["gpt-4.1-nano"] = "gpt-4.1-nano"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-4.1-nano"

class OptionModelGpt4o(Config):
    name: Literal["gpt-4o"] = "gpt-4o"
    value: Literal["gpt-4o"] = "gpt-4o"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-4o"

class OptionModelGpt4oMini(Config):
    name: Literal["gpt-4o-mini"] = "gpt-4o-mini"
    value: Literal["gpt-4o-mini"] = "gpt-4o-mini"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "gpt-4o-mini"


class OptionReasoningNone(Config):
    name: Literal["none"] = "none"
    value: Literal["none"] = "none"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "none"

class OptionReasoningMinimal(Config):
    name: Literal["minimal"] = "minimal"
    value: Literal["minimal"] = "minimal"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "minimal"

class OptionReasoningLow(Config):
    name: Literal["low"] = "low"
    value: Literal["low"] = "low"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "low"

class OptionReasoningMedium(Config):
    name: Literal["medium"] = "medium"
    value: Literal["medium"] = "medium"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "medium"

class OptionReasoningHigh(Config):
    name: Literal["high"] = "high"
    value: Literal["high"] = "high"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "high"

class OptionReasoningXhigh(Config):
    name: Literal["xhigh"] = "xhigh"
    value: Literal["xhigh"] = "xhigh"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "xhigh"


class OptionDetailAuto(Config):
    name: Literal["auto"] = "auto"
    value: Literal["auto"] = "auto"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "auto"

class OptionDetailLow(Config):
    name: Literal["low"] = "low"
    value: Literal["low"] = "low"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "low"

class OptionDetailHigh(Config):
    name: Literal["high"] = "high"
    value: Literal["high"] = "high"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"
    class Config:
        title = "high"




class ModelVersion(Config):
    name: Literal["ModelVersion"] = "ModelVersion"
    value: Union[OptionModelGpt54, OptionModelGpt52, OptionModelGpt51, OptionModelGpt5, OptionModelGpt5Mini, OptionModelGpt5Nano, OptionModelGpt41, OptionModelGpt41Mini, OptionModelGpt41Nano, OptionModelGpt4o, OptionModelGpt4oMini]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"
    class Config:
        title = "Model Version"
        json_schema_extra = {"shortDescription": "OpenAI model to use"}

class ApiKey(Config):
    name: Literal["ApiKey"] = "ApiKey"
    value: str = Field(default="")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "API Key"
        json_schema_extra = {"shortDescription": "OpenAI API Key"}

class Temperature(Config):
    name: Literal["Temperature"] = "Temperature"
    value: float = Field(ge=0.0, le=2.0, default=0.7)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0.0, 2.0]"] = "[0.0, 2.0]"
    class Config:
        title = "Temperature"
        json_schema_extra = {"shortDescription": "Sampling temperature"}

class MaxTokens(Config):
    name: Literal["MaxTokens"] = "MaxTokens"
    value: int = Field(default=1024)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Max Tokens"
        json_schema_extra = {"shortDescription": "Maximum tokens to generate"}

class ReasoningEffort(Config):
    name: Literal["ReasoningEffort"] = "ReasoningEffort"
    value: Union[OptionReasoningNone, OptionReasoningMinimal, OptionReasoningLow, OptionReasoningMedium, OptionReasoningHigh, OptionReasoningXhigh]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"
    class Config:
        title = "Reasoning Effort"
        json_schema_extra = {"shortDescription": "Amount of reasoning effort"}

class ImageDetail(Config):
    name: Literal["ImageDetail"] = "ImageDetail"
    value: Union[OptionDetailAuto, OptionDetailLow, OptionDetailHigh]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"
    class Config:
        title = "Image Detail"
        json_schema_extra = {"shortDescription": "Image resolution quality"}

class ConfigPrompt(Config):
    name: Literal["ConfigPrompt"] = "ConfigPrompt"
    value: str = Field(default="")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Prompt"
        json_schema_extra = {"shortDescription": "Text prompt to send"}

class ConfigClasses(Config):
    name: Literal["ConfigClasses"] = "ConfigClasses"
    value: str = Field(default="")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Classes"
        json_schema_extra = {"shortDescription": "Classes to classify or detect (comma-separated)"}

class ConfigOutputStructure(Config):
    name: Literal["ConfigOutputStructure"] = "ConfigOutputStructure"
    value: str = Field(default='{"key": "value"}')
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"
    class Config:
        title = "Output Structure"
        json_schema_extra = {"shortDescription": "Expected JSON output structure"}





class UnconstrainedConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    reasoningEffort: ReasoningEffort
    imageDetail: ImageDetail

class OcrConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class VqaConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class CaptionConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class DetailedCaptionConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class ClassificationConfigs(Configs):
    configprompt: ConfigPrompt
    configclasses: ConfigClasses
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class MultiLabelClassificationConfigs(Configs):
    configprompt: ConfigPrompt
    configclasses: ConfigClasses
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class ObjectDetectionConfigs(Configs):
    configprompt: ConfigPrompt
    configclasses: ConfigClasses
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class StructuredAnsweringConfigs(Configs):
    configprompt: ConfigPrompt
    configoutputstructure: ConfigOutputStructure
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    imageDetail: ImageDetail

class PromptOnlyConfigs(Configs):
    configprompt: ConfigPrompt
    modelVersion: ModelVersion
    apiKey: ApiKey
    temperature: Temperature
    maxTokens: MaxTokens
    reasoningEffort: ReasoningEffort






class UnconstrainedInputs(Inputs):
    inputImage: InputImage


class UnconstrainedOutputs(Outputs):
    output: OutputText

class UnconstrainedRequest(Request):
    inputs: Optional[UnconstrainedInputs]
    configs: UnconstrainedConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class UnconstrainedResponse(Response):
    outputs: UnconstrainedOutputs




class OcrInputs(Inputs):
    inputImage: InputImage


class OcrOutputs(Outputs):
    output: OutputText

class OcrRequest(Request):
    inputs: Optional[OcrInputs]
    configs: OcrConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class OcrResponse(Response):
    outputs: OcrOutputs




class VqaInputs(Inputs):
    inputImage: InputImage


class VqaOutputs(Outputs):
    output: OutputText

class VqaRequest(Request):
    inputs: Optional[VqaInputs]
    configs: VqaConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class VqaResponse(Response):
    outputs: VqaOutputs



class CaptionInputs(Inputs):
    inputImage: InputImage


class CaptionOutputs(Outputs):
    output: OutputText

class CaptionRequest(Request):
    inputs: Optional[CaptionInputs]
    configs: CaptionConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class CaptionResponse(Response):
    outputs: CaptionOutputs



class DetailedCaptionInputs(Inputs):
    inputImage: InputImage


class DetailedCaptionOutputs(Outputs):
    output: OutputText

class DetailedCaptionRequest(Request):
    inputs: Optional[DetailedCaptionInputs]
    configs: DetailedCaptionConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class DetailedCaptionResponse(Response):
    outputs: DetailedCaptionOutputs





class ClassificationInputs(Inputs):
    inputImage: InputImage


class ClassificationOutputs(Outputs):
    output: OutputText
    classes: OutputClasses


class ClassificationRequest(Request):
    inputs: Optional[ClassificationInputs]
    configs: ClassificationConfigs
    class Config:
        json_schema_extra = {"target": "configs"}


class ClassificationResponse(Response):
    outputs: ClassificationOutputs

class MultiLabelInputs(Inputs):
    inputImage: InputImage


class MultiLabelOutputs(Outputs):
    output: OutputText
    classes: OutputClasses

class MultiLabelClassificationRequest(Request):
    inputs: Optional[MultiLabelInputs]
    configs: MultiLabelClassificationConfigs
    class Config:
        json_schema_extra = {"target": "configs"}
class MultiLabelClassificationResponse(Response):
    outputs: MultiLabelOutputs

class ObjectDetectionInputs(Inputs):
    inputImage: InputImage


class ObjectDetectionOutputs(Outputs):
    output: OutputText
    classes: OutputClasses


class ObjectDetectionRequest(Request):
    inputs: Optional[ObjectDetectionInputs]
    configs: ObjectDetectionConfigs
    class Config:
        json_schema_extra = {"target": "configs"}
class ObjectDetectionResponse(Response):
    outputs: ObjectDetectionOutputs

class StructuredAnsweringInputs(Inputs):
    inputImage: InputImage


class StructuredAnsweringOutputs(Outputs):
    output: OutputText

class StructuredAnsweringRequest(Request):
    inputs: Optional[StructuredAnsweringInputs]
    configs: StructuredAnsweringConfigs
    class Config:
        json_schema_extra = {"target": "configs"}
class StructuredAnsweringResponse(Response):
    outputs: StructuredAnsweringOutputs

class PromptOnlyOutputs(Outputs):
    output: OutputText

class PromptOnlyRequest(Request):

    configs: PromptOnlyConfigs
    class Config:
        json_schema_extra = {"target": "configs"}

class PromptOnlyResponse(Response):
    outputs: PromptOnlyOutputs



class OpenaiUnconstrainedExecutor(Config):
    name: Literal["OpenaiUnconstrained"] = "OpenaiUnconstrained"
    value: Union[UnconstrainedRequest, UnconstrainedResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Unconstrained"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiOcrExecutor(Config):
    name: Literal["OpenaiOcr"] = "OpenaiOcr"
    value: Union[OcrRequest, OcrResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "OCR"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiVqaExecutor(Config):
    name: Literal["OpenaiVqa"] = "OpenaiVqa"
    value: Union[VqaRequest, VqaResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Visual Question Answering"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiCaptionExecutor(Config):
    name: Literal["OpenaiCaption"] = "OpenaiCaption"
    value: Union[CaptionRequest, CaptionResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Caption"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiDetailedCaptionExecutor(Config):
    name: Literal["OpenaiDetailedCaption"] = "OpenaiDetailedCaption"
    value: Union[DetailedCaptionRequest, DetailedCaptionResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Detailed Caption"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiClassificationExecutor(Config):
    name: Literal["OpenaiClassification"] = "OpenaiClassification"
    value: Union[ClassificationRequest, ClassificationResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Classification"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiMultiLabelClassificationExecutor(Config):
    name: Literal["OpenaiMultiLabelClassification"] = "OpenaiMultiLabelClassification"
    value: Union[MultiLabelClassificationRequest, MultiLabelClassificationResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Multi-Label Classification"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiObjectDetectionExecutor(Config):
    name: Literal["OpenaiObjectDetection"] = "OpenaiObjectDetection"
    value: Union[ObjectDetectionRequest, ObjectDetectionResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Object Detection"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiStructuredAnsweringExecutor(Config):
    name: Literal["OpenaiStructuredAnswering"] = "OpenaiStructuredAnswering"
    value: Union[StructuredAnsweringRequest, StructuredAnsweringResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Structured Answering"
        json_schema_extra = {"target": {"value": 0}}

class OpenaiPromptOnlyExecutor(Config):
    name: Literal["OpenaiPromptOnly"] = "OpenaiPromptOnly"
    value: Union[PromptOnlyRequest, PromptOnlyResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    class Config:
        title = "Prompt Only"
        json_schema_extra = {"target": {"value": 0}}


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[
        OpenaiUnconstrainedExecutor, OpenaiOcrExecutor, OpenaiVqaExecutor, OpenaiCaptionExecutor, OpenaiDetailedCaptionExecutor,
        OpenaiClassificationExecutor, OpenaiMultiLabelClassificationExecutor, OpenaiObjectDetectionExecutor, OpenaiStructuredAnsweringExecutor,
        OpenaiPromptOnlyExecutor
    ]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    class Config:
        title = "Task"

class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["capsule"] = "capsule"
    name: Literal["Openai"] = "Openai"
