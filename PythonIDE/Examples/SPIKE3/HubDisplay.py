import display, time

display.display_clear()

(row,col,bright) = (1,2,100)
display.display_set_pixel(col,row,bright)
print(display.display_get_pixel(row,col))
display.display_text_for_time('fred',1000,100)  # sort of works


#display.display_invert() not working
#display.display_set_orientation(90) not working
#display.display_show_pictogram(3) not working
