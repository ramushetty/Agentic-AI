import multiprocessing
import time 

def analyze_image(image_name,result_queue):
    print(f"analyzing {image_name} ....")

    # simulated detection result
    people_detected= 4

    result_queue.put({
        "image": image_name,
        "people": people_detected
    })

if __name__ == "__main__":

    results = multiprocessing.Queue()

    # creates process object
    process = multiprocessing.Process(
        target=analyze_image,
        args=("factory_cam_01.jpg", results)
    )

    process.start()
    process.join()

    result = results.get()
    print("Result received by main process:",result)
