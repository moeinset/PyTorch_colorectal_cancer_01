#for using in modular mode:

#### 1-download data to your colab (you can use get_data.py module)
data should be in this order:

"
data/
  tumor_stroma_lympho/
    train/
      tumor/
        train_image_01.jpeg
        train_image_02.jpeg
        ...
      stroma/
      lympho/
    test/
      tumor/
        test_image_01.jpeg
        test_image_02.jpeg
        ...
      stroma/
      lympho/
      
      "
      
#### 2-edit train.py and define "Hyperparameters" (you can change):
NUM_EPOCHS 
BATCH_SIZE 
HIDDEN_UNITS
LEARNING_RATE

#### 3-save train.py

#### 4-execute train.py in script mode and enjoy training ;)

#### 5- the model will be saved in model directory
