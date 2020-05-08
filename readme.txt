Hi Guys. This code is written to help those starters who wanted to obtain their own custom dataset from the Cifar100 dataset.
Requirements:
* keras
* python interpretor(3.7 and up)
The Constants used in the code:
  Cifar100 has 50000 images of dimension 32*32 which are divided into 20 Superclasses/100 classes. Names of 
  the super classes and classes are given in Labels_coarse and Labels_fine lists respectively.
  no_of_classes: The number of classes of which you want to create the custom dataset
Your custom data set will be stored in files names 'Image_data' and 'Labels'.You can use them by using load method
of pickle.
