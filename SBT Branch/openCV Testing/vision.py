import cv2 as cv
import numpy as np

class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None
    txt = 'null'

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED, text='null'):
        # load the image we're trying to match
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_COLOR)
        if text == 'null':
            self.txt = needle_img_path.split('.')
            self.txt = self.txt[0]
            self.txt = self.txt.split('\\')
            self.txt = self.txt[2]
        else:
            self.txt = text.split('.')
            self.txt = self.txt[0]
        # save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # there are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def draw_text(self, img, text='null',
            font=cv.FONT_HERSHEY_COMPLEX_SMALL,
            pos=(0, 0),
            font_scale=0.5,
            font_thickness=1,
            text_color=(255, 255, 255),
            text_color_bg=(0, 0, 0)
            ):
        text = self.txt
        x, y = pos
        text_size, _ = cv.getTextSize(text, font, font_scale, font_thickness)
        text_w, text_h = text_size
        cv.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
        cv.putText(img, text, (x, int(y + text_h + font_scale - 1)), font, font_scale, text_color, font_thickness)
        return text_size

    def find(self, haystack_img, threshold=0.5, debug_mode=None, test=False, type='Default'):
        # run the OpenCV algorithm        
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)
        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        #print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        #print(rectangles)

        # Choose the line color
        if type == 'Default' or type == 'UI':
            line_color = (0, 255, 0)
        elif type == 'Pet':
            line_color = (128, 0, 128)
        elif type == 'Food':
            line_color = (0, 0, 0)
        elif type == 'Team':
            line_color = (255,0,0)


        points = []
        if len(rectangles):
            #print('Found needle.')
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                
                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)

                # Save the points
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, 
                                lineType=line_type, thickness=2)
                    # cv.putText(haystack_img, self.txt, top_left, cv.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 0), 1, cv.LINE_AA, False)
                    self.draw_text(img=haystack_img, pos=top_left, text_color_bg=line_color)
                elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(haystack_img, (center_x, center_y), 
                                color=marker_color, markerType=marker_type, 
                                markerSize=40, thickness=2)

        if debug_mode:
            cv.imshow('Matches', haystack_img)

        return self.txt, points