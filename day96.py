import time
import asyncio
import requests
async def function1():
    import requests
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    
    print("func1")

async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content)
    print("func2")

async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    print("func3")

async def main():
   l=await asyncio.gather(  function1(),
                            function2(),
                            function3())
      
asyncio.run(main())