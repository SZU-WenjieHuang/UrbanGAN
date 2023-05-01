### UrbanGAN: A GAN based model for predicting the popularity of second-hand housing (2021.8-2021.10)
  ***Repository:*** [UrbanGAN](https://github.com/SZU-WenjieHuang/UrbanGAN)\
  ***Dataset:*** [POI Data in Shanghai from Amap.api / 6000 Second-hand-houses data from Lianjia.com / Graphs Data from ArcGis](https://drive.google.com/drive/folders/1oKqr5l3vJyV593nsufG4iYxftGv5rAum?usp=sharing)\
  ***Description:*** A summer project at TongJi University supervised by Professor Hao Zheng. Using the API of Amap to collect POI (Points of interests) data of Shanghai, including school, hospital, underground station, bus station ,business and shopping center's location. And the popularity data of second-hand houses from Lianjia website. Trying to use GAN to train an image-to-image mapping to learn the impact of POI data on the popularity of second-hand housing.
  
- #### [Datasets](https://drive.google.com/drive/folders/1oKqr5l3vJyV593nsufG4iYxftGv5rAum?usp=sharing)
  ![image](https://user-images.githubusercontent.com/82434538/235452950-3102bbf3-5911-4e84-8cd0-f8b4d35d768f.png)\
  ***POI (Points of Interest) Data (From Amap.api)***\
  ***Index:*** Index of second-hand houses in Shanghai.(Total 6000).\
  ***location:*** Longitude and latitude of each sample.\
  ***Hospnums:*** Number of hospitals within 1000m.\
  ***Subnumbs:*** Number of Subway Stations within 800m.\
  ***Edubumbs:*** Number of Schools within 500m.\
  ***Total_Price:*** The price of the whole house.\
  ***Unit_Price:*** Unit price per square meter.\
  ***Follow_Count:*** Number of followers on lianjia.com.</p>
  ![image](https://user-images.githubusercontent.com/82434538/235453014-f31812b0-303f-4d0f-bfc6-86b2f5bcbd9d.png)
  ***Graphs Data (From Baidu Map &ArcGis)***\
  ***District Centroid Distance:*** Sum of coefficients of sample distance from each urban center. ( Closest 5 Urban Center)\
  ***Househeat:*** Househeat(θ) = α / log (β） α = Number of followers on lianjia.com. β = Duration on sale. *Numbs are Based on the service radius of each POI point.</p>

- #### Pipeline
  ![image](https://user-images.githubusercontent.com/82434538/235453828-e8631198-e9ba-4f63-9927-661dd1d3b0eb.png)\
  ***Date Collecting*** Collect data from Amap API, Lianjia official website, and ArcGIS using Python.</p>
  ![image](https://user-images.githubusercontent.com/82434538/235455811-a2f61b47-43f9-40a0-ad14-3617b65e1188.png)
  ***Data Processing*** After performing exploratory data analysis (EDA) on different types of POI data, the data is visualized on a single JPG image with a resolution of 8000*8000. Similarly, the HouseHeat data (a measure of the popularity of second-hand houses obtained from a defined company) is also visualized and represented on an 8000*8000 JPG image. These POI and HouseHeat JPG images are then segmented into 225 512*512 images to create a dataset. Our objective is to establish a mapping from the POI images to the HouseHeat images.</p>
  ![image](https://user-images.githubusercontent.com/82434538/235455638-6d09924e-33af-4d38-9e01-e6b6d64b5b8a.png)
  ***Model Training*** We trained a GAN to learn a mapping between two images stes, also known as an image-to-image translation.</p>
  ***Pridiction*** In our study, we employed the model trained on the Shanghai dataset to predict the HouseHeat image data of other major Chinese cities, such as Beijing and Shenzhen, due to the fact that these cities share very similar factors that influence people's choices of housing location.


- #### Training
  During the training process, we primarily employed various visualization techniques to construct the model, attempting to find the optimal visual methods that the model can learn best from.
  ![image](https://user-images.githubusercontent.com/82434538/235456136-91b1d365-f876-4624-bcfc-1f0467a6628a.png)
  ![image](https://user-images.githubusercontent.com/82434538/235456190-642d41c9-aa94-4fc3-9e98-b4968378acaa.png)
  ![image](https://user-images.githubusercontent.com/82434538/235456521-7ea0df04-d63a-4038-b34f-5309345086d9.png)
  ![image](https://user-images.githubusercontent.com/82434538/235456279-b6d4eeb4-5871-4e19-a80b-9f895649888c.png)
  ![image](https://user-images.githubusercontent.com/82434538/235456333-361d9817-f890-4326-8670-8cf9e9b80ff7.png)
  Using different RGB colors to represent different POI types and grayscale shades to represent HouseHeat values, and adding a mask to the visualization image to remove areas where second-hand houses are impossible to exist (such as rivers and lakes), we found that this approach can get the best prediction results.

- #### Prediction
  Using the POI dataset from Beijing as the test set, we found that the model achieved very good results on this dataset.
  ![image](https://user-images.githubusercontent.com/82434538/235457225-6e2f6196-3cae-404c-8423-35fbded1feae.png)
  
