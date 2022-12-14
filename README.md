# A Deep learning model for colorectal cancer histopathological images classifying : using convolutional neural network (CNN) 

#### Introduction: 
The study of tissue by histopathology is regarded as the gold standard for determining a cancer's prognosis. The scanning and digitizing of whole histology slides is known as whole-slide imaging (WSI), and it is currently being used in pathology labs all over the world. Analyzing these images takes time due to the complexity of WSIs and the rise in the number of suspected cancer cases. Automated diagnosis of tumorous tissue helps in elevating the precision, speed, and reproducibility of research. Deep learning-based methods have recently produced cutting-edge outcomes for a number of image analysis applications, including the interpretation of digital slides. in this work we try to training a deep learning model that can classify tumor, stroma and lympho using pathology images.
#### Method: 
The dataset for this study was obtained from a free full-slide imaging database that contained colorectal cancer pathology images. We used three categories of this dataset, Tumor, stroma and lympho slides. All data divided into training and testing datasets each included 500 and 125 images, respectively. Train and test datasets were in different folders. Image patches are usually square regions with dimensions ranging from 32 × 32 pixels up to 10,000 × 10,000 pixels. We used image patches of around 64 × 64 pixels. This approach to reducing the high dimensionality of WSIs can be seen as human guided feature selection. Also an augmentation built in method, TrivialAugmentWide , was used for improving the results. All data converted to tensor by PyTorch utilities to become compatible with PyTorch framework. For avoiding memory overwhelming and optimized training, data grouped in 32 batch size. A model using convolutional neural network (CNN) was designed in two blocks of (CNN-layer->ReLU->CNN-layer->ReLU->MaxPool) followed by a linear classifier. The model was trained 40 times, using cross entropy loss function and ADAM optimizer. the accuracy and loss were calculated and plotted. 
#### Results:
The results showed a convergence after about 10 epochs and were continued by other epochs. Train's loss reduced from 1.0290 to 0.2658 after complete training, and the accuracy increased from 0.4651 to 0. 8941.Test's loss also reduced from 0.7104 to 0.1166, and the accuracy increased from 0.6392 to 0.9719.
#### Discussion:
As we see our model present a good accuracy about 90 percent. but we still can improve the model by increasing hidden layers, changing activation function, using more data and change learning algorithm parameters. By designing and training different models and using different data, a model can be presented to help pathologists for better diagnosis and reduce time.

.
Note : because of the data server policity the exact link of data may be changed!
so update the data link by copy address from the data server!

data available here : https://cdn-119.anonfiles.com/8ep9p1F8y5/5147761f-1667854476/tumor_stroma_lympho.zip
code available at : https://github.com/moeinset/PyTorch_colorectal_cancer_01
