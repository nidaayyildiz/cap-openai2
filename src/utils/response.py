from sdks.novavision.src.helper.package import PackageHelper
from capsules.Openai.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor,
    OutputText, OutputClasses, OpenaiUnconstrainedExecutor,  UnconstrainedOutputs, UnconstrainedResponse, OpenaiOcrExecutor, 
    OcrResponse, OcrOutputs, OpenaiVqaExecutor, VqaResponse, VqaOutputs, OpenaiCaptionExecutor, CaptionResponse, CaptionOutputs, 
    OpenaiDetailedCaptionExecutor, DetailedCaptionResponse, DetailedCaptionOutputs, OpenaiMultiLabelClassificationExecutor, MultiLabelClassificationResponse,
    MultiLabelOutputs, OpenaiClassificationExecutor, ClassificationResponse, ClassificationOutputs, OpenaiPromptOnlyExecutor,
    PromptOnlyResponse, PromptOnlyOutputs, OpenaiStructuredAnsweringExecutor, StructuredAnsweringResponse, StructuredAnsweringOutputs,
    OpenaiObjectDetectionExecutor, ObjectDetectionResponse, ObjectDetectionOutputs 

)

def build_unconstrained_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = UnconstrainedOutputs(output=output_text)
    response = UnconstrainedResponse(outputs=outputs)
    executor = OpenaiUnconstrainedExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_ocr_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = OcrOutputs(output=output_text)
    response = OcrResponse(outputs=outputs)
    executor = OpenaiOcrExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_vqa_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = VqaOutputs(output=output_text)
    response = VqaResponse(outputs=outputs)
    executor = OpenaiVqaExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_caption_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = CaptionOutputs(output=output_text)
    response = CaptionResponse(outputs=outputs)
    executor = OpenaiCaptionExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_detailed_caption_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DetailedCaptionOutputs(output=output_text)
    response = DetailedCaptionResponse(outputs=outputs)
    executor = OpenaiDetailedCaptionExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_classification_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)
    outputs = ClassificationOutputs(output=output_text, classes=classes)
    response = ClassificationResponse(outputs=outputs)
    executor = OpenaiClassificationExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_multi_label_classification_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)
    outputs = MultiLabelOutputs(output=output_text, classes=classes)
    response = MultiLabelClassificationResponse(outputs=outputs)
    executor = OpenaiMultiLabelClassificationExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_object_detection_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)  # Using parsed structures
    outputs = ObjectDetectionOutputs(output=output_text, classes=classes)
    response = ObjectDetectionResponse(outputs=outputs)
    executor = OpenaiObjectDetectionExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_structured_answering_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = StructuredAnsweringOutputs(output=output_text)
    response = StructuredAnsweringResponse(outputs=outputs)
    executor = OpenaiStructuredAnsweringExecutor(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_prompt_only_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = PromptOnlyOutputs(output=output_text)
    promptOnlyResponse = PromptOnlyResponse(outputs=outputs)
    executor = OpenaiPromptOnlyExecutor(value=promptOnlyResponse)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)
