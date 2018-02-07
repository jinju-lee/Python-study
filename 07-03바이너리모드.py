k_image=open('c:/koala.jpg','rb')
k_image_2=open('c:/koala_2.jpg','wb')
print(k_image_2.write(k_image.read()))

k_image.close()
k_image_2.close()
