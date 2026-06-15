import multiprocessing
import requests


def downloadfile(url,name):
     print(f"Starting download file {name}")
     response = requests.get(url)
     open(f"file{name}.jpg", "wb").write(response.content)
     print(f"Fininshed download file {name}")
     
     
if __name__ == '__main__':  
    url="https://picsum.photos/200/300"
    pros=[]
    for i in range(5):
        # downloadfile(url,i)
        
        # Multiprocessing
        p=multiprocessing.Process(target=downloadfile,args=[url,i])
        p.start()
        pros.append(p)
        
    for p in pros:
        p.join()
        
