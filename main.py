
import tensorflow as tf
import numpy as np
from queue import Queue
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog



model = tf.keras.models.load_model("magenta_arbitrary-image-stylization-v1-256_2")


def run_inference():
    content_image = label_1_array.get_item().astype(np.float32)[np.newaxis, ...] / 255.0
    style_image = label_2_array.get_item().astype(np.float32)[np.newaxis, ...] / 255.0
    outputs = model(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]
    image = (stylized_image[0].numpy()*255).astype(np.uint8)
    image = ImageTk.PhotoImage(Image.fromarray(image).resize((550,335)))
    generated_img_label.configure(image = image)
    generated_img_label.image = image
    


#Function to load images for content and style
label_1_array = Queue()
label_2_array = Queue()
def openfile(img_label):
    img_path = filedialog.askopenfile(title='Please select an image',
                           filetypes=[('Image Files', ['.jpeg', '.jpg', 
                                                        '.png'
                                                       ])])
    
    if img_label==label:
        print("Label 1")
        label_1_array.clear()
        label_1_array.enqueue(np.asarray(Image.open(img_path.name).resize((256, 256))))
    else:
        print("Label 2")
        label_2_array.clear()
        label_2_array.enqueue(np.asarray(Image.open(img_path.name).resize((256, 256))))
    
    img = ImageTk.PhotoImage(Image.open(img_path.name).resize((200,200)))
    img_label.configure(image=img)
    img_label.image=img




#Main window
artist = Tk()
artist.title("Art Generator")
artist.geometry("720x695+150+0")
artist.resizable(width=False, height=False)
artist.config(bg="black")

#Content Frame to place images
content_frame = Frame(artist, width=720, height=300, bg="magenta")
content_frame.place(x=0, y=0)
#Image 1
img = ImageTk.PhotoImage(Image.open("img.png").resize((200,200)))
label = Label(content_frame, image = img)
label.place(x=100, y=0)

#Directory show  Button
button1 = Button(content_frame, text="Select Content Image", command=lambda :openfile(label))
button1.place(x=150, y=250)


#Image 2
#img2 = ImageTk.PhotoImage(Image.fromarray(np.uint8(zeros)).resize((200,200)))
img2 = ImageTk.PhotoImage(Image.open("img.png").resize((200,200)))
label2 = Label(content_frame, image = img2)
label2.place(x=400, y=0)

#Directory showing Button
button2 = Button(content_frame, text="Select Style Image", command=lambda :openfile(label2))
button2.place(x=460, y=250)

#Generate Button Art
run_model_button = Button(content_frame, text="Run Model", bg="green", command=run_inference)
run_model_button.place(x=300, y=250)
#Art Generated Label
generated_label = Label(artist, text="Art Generated Image", bg='black', fg='white', font=("Helvetica",18,"bold")).place(x=220, y=318)
generated_img = ImageTk.PhotoImage(Image.open("img.png").resize((550,335)))
#Generated Image
generated_img_label = Label(artist, image = generated_img)
generated_img_label.place(x=80, y=350)

#Mainloop to keep app running
artist.mainloop()
