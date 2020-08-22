# Get all index of a value in a list
l = [1,2,3,1,1]
[index for index, value in enumerate(l) if value == 1] #find all index of 1 in list l


# Get all index of a value in a list use numpy
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0] # [0] because ii = (arr[],...)


# connect video on phone to lap use app ipwebcam 
url = 'https://192.168.1.11:8080/video'
cap = cv.VideoCapture(url)
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.namedWindow('frame', cv.WINDOW_NORMAL)
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
