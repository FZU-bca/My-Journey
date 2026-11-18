try:
    print(1)
except Exception as e:
    print(e)
else:
    print("No error")
#sentence "else" is not must condition
finally:
    f.close()
#Whenever there are error the finally sentence will be runed