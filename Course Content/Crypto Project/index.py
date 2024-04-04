# Cryptography Project

# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2024-04-04 15:44:42
# @Last Modified by:   undefined
# @Last Modified time: 2024-04-04 15:44:42
# @Description: file:///Users/aj/Desktop/bootcamp/Scrimba/scrimba-python/Course%20Content/Crypto%20Project/index.py
# 
# pseudocode:
    # create keys string
    # autogenerate the values string by offsetting original string
    # create two dictionaries
    #user input 'the message' and mode
    # run encode or decode
    # return result
    # clean and beautify the code 
print("** Project - Crypto **")

def enigma_light():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    
    # autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    
    print(keys, values)
    
enigma_light()








