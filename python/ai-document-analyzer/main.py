
instructions = "You are a helpful assistant that will answer questions based on the content of the document provided. If the answer is not in the document, respond with 'I don't know'."
def load_doc(path):
    # path = input("enter your doc path: ")

    try:
        with open(path,"r") as file: 
            print(f"file loaded sucessfully {file.name}")

            # option = input("options r, a: ")

            # if option == "r":
            content = file.read()
            print(content)
            # if option == "a":
            #     pass
            return content
    except FileNotFoundError:
        print("file not found")
        return None



    {"document_type": "text", 
     "keypoints": ["keypoint1", "keypoint2"], 
     "summary": "This is a summary of the document."}