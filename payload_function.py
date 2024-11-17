import json

def extract_parameters_with_value(value, file_path='output.json', target_value="C1"):
    """
    Loads JSON data from a file and extracts 'parameters' arrays that contain a specific value.
    """
    try:
        # Load JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Access the 'features' array, and then each feature's 'parameters' array
        features = data.get("features", [])
        matching_parameters = []

        for feature in features:
            # Get the 'parameters' array for each feature, if it exists
            parameters = feature.get("parameters", [])
            
            # Check if any entry in 'parameters' has the 'value' key with the target value
            if any(param.get("value") == target_value for param in parameters):
                # Modify 'lengthValue' parameter within parameters array
                for param in parameters:
                    if param.get("parameterId") == "lengthValue" or param.get("parameterId") == "value" :
                        param["expression"] = f"{value} mm"
                
                # Append the modified parameters array to matching_parameters
                matching_parameters.extend(parameters)
        
        return matching_parameters  # This returns only the matching parameters arrays

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not in valid JSON format.")
        return None

# Example usage
parameters_with_c1 = extract_parameters_with_value(file_path='output.json', target_value="C1", value=3)
print(parameters_with_c1)  # Prints the extracted parameters containing "value": "C1" for value 3

def return_payload_feature1_dict(id, value):
    payload1 = {"btType": "BTFeatureDefinitionCall-1406",
          "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : extract_parameters_with_value(file_path='output.json', target_value="C1", value=value)}}
    
    return payload1

def return_payload_feature2_dict(id, value):
    payload2 = {"btType": "BTFeatureDefinitionCall-1406",
          "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : extract_parameters_with_value(file_path='output.json', target_value="C2", value=value)}}
    
    return payload2

def return_payload_feature3_dict(id, value):
    payload3 = {"btType": "BTFeatureDefinitionCall-1406",
          "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : extract_parameters_with_value(file_path='output.json', target_value="C3", value=value)}}
    
    return payload3

def return_payload_feature4_dict(id, value):
    payload4 = {"btType": "BTFeatureDefinitionCall-1406",
          "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : extract_parameters_with_value(file_path='output.json', target_value="C4", value=value)}}
    
    return payload4