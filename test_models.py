#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test custom model configuration
"""

import os
import sys
sys.path.append('.')

from src.utils.llm.models import list_available_models

def test_models():
    print("Testing model configuration...")
    
    # Check environment variables
    print("\nEnvironment variables:")
    env_vars = [
        "MODELSCOPE_API_KEY",
        "DASHSCOPE_API_KEY", 
        "ZHIPUAI_API_KEY",
        "OPENAI_API_KEY"
    ]
    
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print("✅ " + var + ": Set")
        else:
            print("❌ " + var + ": Not set")
    
    # Check model list
    print("\nModel list:")
    try:
        models = list_available_models()
        print("Total models: " + str(len(models)))
        
        custom_models = [m for m in models if m['provider'] == 'custom']
        print("Custom models: " + str(len(custom_models)))
        
        print("\nCustom model details:")
        for model in custom_models:
            status = "✅" if model['api_key_available'] else "❌"
            print(status + " " + model['display_name'] + " (" + model['model_name'] + ")")
            
    except Exception as e:
        print("❌ Error: " + str(e))

if __name__ == "__main__":
    test_models()