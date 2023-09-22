def setup():
    size(500,500)
    
def  draw():
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
        
        
