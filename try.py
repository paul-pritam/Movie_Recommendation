import os
import cv2
import matplotlib.pyplot as plt


from mtcnn import MTCNN
detector = MTCNN()

video = cv2.VideoCapture("a.mp4")

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(video.get(cv2.CAP_PROP_FPS))
c=video.get(cv2.CAP_PROP_FRAME_COUNT)
# result = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), fps, (width, height), isColor=False)

frame_num = 0
count=0
while (c>frame_num):

    ret, frame = video.read()

    frame_num += 1

    if ret:

        location = detector.detect_faces(frame)

        if len(location) > 0:
            for face in location:
                x, y, w, h = face['box']
                x2, y2 = x + w, y + h

                cv2.rectangle(frame, (x, y), (x2, y2), (255, 255,255), 1)
                rec = frame[y:y2, x:x2]
                # print(frame_num)
                # try:
                cv2.imwrite('face_{}'.format(count) + '.jpg', rec)
                count+=1

                # except:
                #     pass
                # cv2.imshow(rec)
                # result.write(frame)
                cv2.imshow("result",frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


        else:
            break
print(count)
cv2.destroyAllWindows()
video.release()
# result.release()



