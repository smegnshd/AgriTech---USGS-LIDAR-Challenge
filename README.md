my_lidar_AgriTec python package
This is simple python package called my_lidar_AgriTec' used to read, transform and visualize LIDAR cloud data using public data path: https://s3-us-west-2.amazonaws.com/usgs-lidar-public/.

a)	What it did? 
This package:
1.	Read public data path and change to ept.json file.
2.	Generate pipeline.json file using Pdal, and recive back .tif and .laz files.
3.	Transform .tiff/ laz data
4.	Visualize data .
b)	Installation 
Install by using:
                     “pip install my_lidar”
or 
      “ git clone https://github.com/smegnshd/my_lidar_AgriTec”
Future plan
Develop water flow pipeline framework for data transformation and machine learning.
•	train a model
•	test a model
Example
Public data path with file name: "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/IA_FullState/ept.json"
With "bounds": "([-10425171.940, -10423171.940], [5164494.710, 5166494.710])",
see Raw data: https://github.com/smegnshd/my_lidar_AgriTec/blob/main/image/iowa-color.png 

 




	
	
