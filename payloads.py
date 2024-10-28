# This is for setting parameters

def return_payload_feature1_dict(id, value):
  payload1 = {"btType": "BTFeatureDefinitionCall-1406",
          "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : [ {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "M4i57bsHsMqZhiOnI",
            "parameterId" : "initEntities"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "MnDwqZ8pWgJ2dfmAO",
            "enumName" : "VariableMode",
            "value" : "ASSIGNED",
            "parameterId" : "mode"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "MdnRrwUKjqoA00SJe",
            "enumName" : "VariableType",
            "value" : "LENGTH",
            "parameterId" : "variableType"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "M4niR/6caCjPh3Z3V",
            "enumName" : "VariableMeasurementMode",
            "value" : "DISTANCE",
            "parameterId" : "measurementMode"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "C1",
            "nodeId" : "MlSYdRkfgRt/zC3XT",
            "parameterId" : "name"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "MB14S9CpxriJkcmDu",
            "parameterId" : "lengthValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*deg",
            "nodeId" : "M0OXpUurDvkJ/ogvM",
            "parameterId" : "angleValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0",
            "nodeId" : "MnS5ahT1Lo2qcPb5J",
            "parameterId" : "numberValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "MgbZwq8ScDCwRJOXk",
            "parameterId" : "anyValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "M4hibMWtmLrdUu9+c",
            "parameterId" : "value"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "MQmKxDdzn24P+GO03",
            "parameterId" : "entityCouple"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "MDV/MuXmghUrw1rb4",
            "enumName" : "VariableMinMaxSelection",
            "value" : "MINIMUM",
            "parameterId" : "minmax"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "MpXuQabCYxxm/TEq6",
            "parameterId" : "extendEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "M5qnoHGnkt7lZZ/1F",
            "parameterId" : "measureFromAxis"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*mm",
            "nodeId" : "MTq7Qoi+lP/S1mECG",
            "parameterId" : "distance"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*mm",
            "nodeId" : "MeG7vxANA9FQ+RxzA",
            "parameterId" : "xOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*mm",
            "nodeId" : "MffwFCh/5/VHquqHj",
            "parameterId" : "yOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*mm",
            "nodeId" : "M20wRAAxagRMOMl8L",
            "parameterId" : "zOffset"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "M319rpmecuFRrnvt4",
            "enumName" : "AxisWithCustom",
            "value" : "DISTANCE",
            "parameterId" : "componentSelector"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "MFEF0h0u09WBRd0cK",
            "parameterId" : "customDirection"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0.0*mm",
            "nodeId" : "MNpQGZ3qz92QBKOeo",
            "parameterId" : "customOffset"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "MoPIbARN9hr7dhiYq",
            "parameterId" : "lengthEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "MEPg0c7fvtu7vt2EE",
            "parameterId" : "radius"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "MUpN3L0nZipM7aL2h",
            "parameterId" : "diameterEntity"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "",
            "nodeId" : "MYgUNe9tu/vo5P81s",
            "parameterId" : "description"
          }]}}
  return payload1


def return_payload_feature2_dict(id, value):
  payload2 = {"btType": "BTFeatureDefinitionCall-1406",
           "feature": 
          {"featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : [ {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "LeVAKpOBwYMm0O+D",
            "parameterId" : "initEntities"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "efqcuSITuvGa3uCk",
            "enumName" : "VariableMode",
            "value" : "ASSIGNED",
            "parameterId" : "mode"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "VFElz2Mb97miElG1",
            "enumName" : "VariableType",
            "value" : "LENGTH",
            "parameterId" : "variableType"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "8t/mJttKHwwtnalj",
            "enumName" : "VariableMeasurementMode",
            "value" : "DISTANCE",
            "parameterId" : "measurementMode"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "C2",
            "nodeId" : "MPRMuQc4NYqIFfVvY",
            "parameterId" : "name"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "YONEPJvvIozbMAwG",
            "parameterId" : "lengthValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 deg",
            "nodeId" : "uwZEmgN+B3y+22JP",
            "parameterId" : "angleValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "BLPoZv2BLa9IrY6u",
            "parameterId" : "numberValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "Hf1icb5MR+/cFT8l",
            "parameterId" : "anyValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "vq1f98WpR6mvwTSZ",
            "parameterId" : "value"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "oUW0ksgILOhMvWf/",
            "parameterId" : "entityCouple"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "AM6ZsodiqFEsmr5S",
            "enumName" : "VariableMinMaxSelection",
            "value" : "MINIMUM",
            "parameterId" : "minmax"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "jAbaproI/mLrCAag",
            "parameterId" : "extendEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "nw0gDK1XVJHuwoz2",
            "parameterId" : "measureFromAxis"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "eLkMvZOUuVOmsSBf",
            "parameterId" : "distance"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "MMyKz6zBWFpMh4is",
            "parameterId" : "xOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "EM5Iv4Dk5P7DgHnf",
            "parameterId" : "yOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "pEknhHaQZX0+St4s",
            "parameterId" : "zOffset"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "AoLUtnbcGpzIcEmk",
            "enumName" : "AxisWithCustom",
            "value" : "DISTANCE",
            "parameterId" : "componentSelector"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "T84yyG3nLYk9WxOQ",
            "parameterId" : "customDirection"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "HC3Y45shILWDNuFb",
            "parameterId" : "customOffset"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "k92469LEHs+/NSYV",
            "parameterId" : "lengthEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "t/kAAm693PjxmE3h",
            "parameterId" : "radius"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "BiU9576ZZJSlQnZE",
            "parameterId" : "diameterEntity"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "",
            "nodeId" : "PEs3FvY4FWyZ7Avp",
            "parameterId" : "description"
          }]}}
  return payload2


def return_payload_feature3_dict(id, value):
  payload3 = {"btType": "BTFeatureDefinitionCall-1406",
           "feature": {
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : [ {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "wmIrfahT+XG3s05b",
            "parameterId" : "initEntities"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "gPJfrh3Jnh8bqWmL",
            "enumName" : "VariableMode",
            "value" : "ASSIGNED",
            "parameterId" : "mode"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "mW+gV5y3qXmEqIW5",
            "enumName" : "VariableType",
            "value" : "LENGTH",
            "parameterId" : "variableType"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "y3MvJMV1gaO+suNg",
            "enumName" : "VariableMeasurementMode",
            "value" : "DISTANCE",
            "parameterId" : "measurementMode"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "C3",
            "nodeId" : "MU3MuVRzP9YWeyGlS",
            "parameterId" : "name"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "PDQ73MoVR8jEDrGm",
            "parameterId" : "lengthValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 deg",
            "nodeId" : "GjOihFJXXUKuGz0W",
            "parameterId" : "angleValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "qolu/2W9Hy0N0ZaW",
            "parameterId" : "numberValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "9sHqBs+OznQ4c+ao",
            "parameterId" : "anyValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "PhLgclOLU+F+fQE0",
            "parameterId" : "value"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "ANVjbHXhcbia7aW4",
            "parameterId" : "entityCouple"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "sQAeeQ0n0SI2IyP+",
            "enumName" : "VariableMinMaxSelection",
            "value" : "MINIMUM",
            "parameterId" : "minmax"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "bP4K80Kj/nE6993T",
            "parameterId" : "extendEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "+GJM4XFV7iic9AJ6",
            "parameterId" : "measureFromAxis"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "KuiUEWiFspKgKXPQ",
            "parameterId" : "distance"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "uQaPfCJGEHcSiuvk",
            "parameterId" : "xOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "wXK68rF2aUi7oMmp",
            "parameterId" : "yOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "Ju9oOe8otb3OMFle",
            "parameterId" : "zOffset"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "3fOKpNi+RAN1szoH",
            "enumName" : "AxisWithCustom",
            "value" : "DISTANCE",
            "parameterId" : "componentSelector"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "+ZlVN54sAFIEtn9E",
            "parameterId" : "customDirection"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "Y4syxfMcmWel5A+x",
            "parameterId" : "customOffset"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "Z1LYXiT3S9f5gKvz",
            "parameterId" : "lengthEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "a5v+7Wzx78Coja1E",
            "parameterId" : "radius"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "30Ir150ViFpGUwsb",
            "parameterId" : "diameterEntity"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "",
            "nodeId" : "9pRdiCWYcT1CE7Ni",
            "parameterId" : "description"
          } ]}}
  return payload3


def return_payload_feature4_dict(id, value):
  payload4 = {"btType": "BTFeatureDefinitionCall-1406",
           "feature":{
          "featureId": id,
          "featureType": "assignVariable",
          "name" : "###name = #value",
          "parameters" : [ {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "1VXDZppKajw6gZ60",
            "parameterId" : "initEntities"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "AE27ZTopyRbw6GTj",
            "enumName" : "VariableMode",
            "value" : "ASSIGNED",
            "parameterId" : "mode"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "xPizGQ1ZTn/CRbZK",
            "enumName" : "VariableType",
            "value" : "LENGTH",
            "parameterId" : "variableType"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "ksvonksFwT7WvPtY",
            "enumName" : "VariableMeasurementMode",
            "value" : "DISTANCE",
            "parameterId" : "measurementMode"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "C4",
            "nodeId" : "MZ/T0CQNnzOZPIoKD",
            "parameterId" : "name"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "nUHGCRq2HNYv43lZ",
            "parameterId" : "lengthValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 deg",
            "nodeId" : "EADGAQIWvQEcf24l",
            "parameterId" : "angleValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "lhld0LnypJ+KCHWk",
            "parameterId" : "numberValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0",
            "nodeId" : "jTNHk3exs2cQAA6h",
            "parameterId" : "anyValue"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : f"{value} mm",
            "nodeId" : "c/ucxw0j3vNfZb1s",
            "parameterId" : "value"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "ifNtKb66A65V/igt",
            "parameterId" : "entityCouple"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "VNc/1yfgQC/EEhM2",
            "enumName" : "VariableMinMaxSelection",
            "value" : "MINIMUM",
            "parameterId" : "minmax"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "7W5Fu3MMQyXGfP0b",
            "parameterId" : "extendEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "DcvnZMYmhXjRqlSd",
            "parameterId" : "measureFromAxis"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "rLIf6dfDATMC3vYK",
            "parameterId" : "distance"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "15bjyJ+vRinHXNgT",
            "parameterId" : "xOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "ZCvMGwIcGO2Kz7ga",
            "parameterId" : "yOffset"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "VJxhys5qViGm0aqU",
            "parameterId" : "zOffset"
          }, {
            "btType" : "BTMParameterEnum-145",
            "namespace" : "",
            "nodeId" : "dn0CtGoDF0NYXZEr",
            "enumName" : "AxisWithCustom",
            "value" : "DISTANCE",
            "parameterId" : "componentSelector"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "zUM2oAHcKG6vdRqP",
            "parameterId" : "customDirection"
          }, {
            "btType" : "BTMParameterQuantity-147",
            "isInteger" : False,
            "value" : 0.0,
            "units" : "",
            "expression" : "0 mm",
            "nodeId" : "dcUOTAAZXcJChgyV",
            "parameterId" : "customOffset"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "e6MnX/Eig4OzVgcJ",
            "parameterId" : "lengthEntities"
          }, {
            "btType" : "BTMParameterBoolean-144",
            "value" : False,
            "nodeId" : "TJG/vi8jTlM/tBG+",
            "parameterId" : "radius"
          }, {
            "btType" : "BTMParameterQueryList-148",
            "queries" : [ ],
            "nodeId" : "BkaXzDrEEf/z0jQ0",
            "parameterId" : "diameterEntity"
          }, {
            "btType" : "BTMParameterString-149",
            "value" : "",
            "nodeId" : "oZCPvkdJgMpN6CZC",
            "parameterId" : "description"
          } ]}}
  return payload4
