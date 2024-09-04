import cv2
import matplotlib.pyplot as plt


trial = cv2.VideoCapture( 1 ,cv2.CAP_ANY)

while False:
    ret, img = cap.read()
    cv2.imshow("input", img)
    cv2.waitKey(0)
    
    
    
    img = cv2.imread('My_first_Repository/python/Prove varie/Unknown.jpeg')
    rgb = cv2.cvtColor( img , cv2.COLOR_BGR2RGB)

    cv2.imshow( "input" , rgb)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print(rgb.shape)

    grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    cv2.imshow( "grey" , grey)
    cv2.waitKey(0)

    cv2.imshow( "angolo",img[0:100 , 100:200])
    cv2.waitKey(0)
    plt.imshow(img[0:200 , 1000:2000])
    plt.show()

def RecordVideo( file_name , duration_s):
    cap = cv2.VideoCapture(1)

    f_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    f_height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int( cap.get( cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter( file_name , fourcc , fps , ( f_width , f_height))
    
    for i in range( 0,fps*duration_s):
        ret, frame = cap.read()
        out.write( frame )

    cap.release()
    out.release()


#RecordVideo( 'try' , 3)

#cap = cv2.VideoCapture('/Users/andreaboldetti/Documents/GitHub/peppino.mp4')

#success , fig = cap.read()
#img = cv2.imread('My_first_Repository/python/Prove varie/Unknown.jpeg')
#rgb = cv2.cvtColor( img , cv2.COLOR_BGR2RGB)

#cv2.imshow( "input" , rgb)
#print( cv2.waitKey(0))


