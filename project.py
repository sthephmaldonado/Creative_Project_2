import json
import random


def lambda_handler(event, context):
    # TODO implement
    
    result = {
            'dialogAction': {
                "type":"Close",
                "fulfillmentState":"Fulfilled",
                "message":{
                    "contentType":"PlainText",
                      }
                }
            }
            
    ##print(event["currentIntent"]["name"])

    
    if event["currentIntent"]["name"] == "HelloIntent" :
        result["dialogAction"]["message"]["content"] 

    elif event["currentIntent"]["name"] == "Sushi" :
        
        Roll = ["California", "Spider", "Eel", "Avocado", "Shrimp Tempura", "Philadelphia", "Spicy Tuna"]
        
        Roll = float(event["currentIntent"]["slots"]["Rolls"]) 
        DeepFrying = float(event["currentIntent"]["slots"]["DeepFrying"])
        Toppings = float(event["currentIntent"]["slots"]["Toppings])
        result["dialogAction"]["message"]["content"] = "You requested:" + Roll+ " " + DeepFrying+ " " +Toppings+ " " 
        
    elif event["currentIntent"]["name"] == "Sides" :
      
        
        Sides=["Seaweed Salad","Crab wonton","Gyoza"]
        
        Side = int(event["currentIntent"]["slots"]["Sides"])
        result["dialogAction"]["message"]["content"] = You requested [side]

       elif event["currentIntent"]["name"] == "Drinks" :
        
        Drinks = int(event["currentIntent"]["slots"]["Drink"])
        result["dialogAction"]["message"]["content"] = You requested [drink]
        
    elif event["currentIntent"]["name"] == "Desserts" :
       
        Dessert = float(event["currentIntent"]["slots"]["Desserts"])
       
    return result;
    
