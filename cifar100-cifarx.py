from keras.datasets import cifar100
import numpy as np
import pickle as pkl

Labels_fine=['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 
    'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 
    'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 
    'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 
    'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 
    'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion',
    'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse',
    'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear',
    'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine',
    'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose',
    'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake',
    'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table',
    'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout',
    'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman',
    'worm']
Labels_coarse=['aquatic_mammals','fish','flowers','food_containers','fruit_and_vegetables',
	'house_hold_electrical_devices','household_furniture','insects','large carnivores',
	'large_man_made_outdoor_things','large_natural_outdoor_scenes','large_omnivores_and_herbivores',
	'medium-sized_mammals','non_insect_invertebrates','people','reptiles','small_mammals','trees',
	'vehicles1','vehicles2']
   
no_of_classes_required=2
total_no_of_images=no_of_classes_required*2500
##Importing Cifar100
(x_train_all,y_train_all),(x_test,y_test)=cifar100.load_data(label_mode='coarse')

##Label_index
p_index=Label_coarse.index('people')
f_index=Label_coarse.index('flower')
##Collecting array address of required images
people=[]
for i in range(0,50000):
    if(y_train_all[i]==p_index): 
        people.append(i)
flowers=[]
for i in range(0,50000):
    if(y_train_all[i]==f_index):
        flowers.append(i)

##creating the dataset
x_train_new=np.ndarray(shape=(total_no_of_images,32,32,3))
y_train_new=np.ndarray(shape=(total_no_of_images,1))

f=0
p=0
c=1
print(f'{len(people)}')

for i in range(0,total_no_of_images):
    if(c==1 and p<2500):
        x_train_new[i]=x_train_all[people[p]]
        y_train_new[i]=0
        p=p+1
        c=0
    else:
        x_train_new[i]=x_train_all[flowers[f]]
        y_train_new[i]=1
        f=f+1
        c=1

##Saving the dataset using pickle
flh1=open('Image_data','wb')
flh2=open('Label','wb')
pkl.dump(x_train_new,flh1)
pkl.dump(y_train_new,flh2)

	
