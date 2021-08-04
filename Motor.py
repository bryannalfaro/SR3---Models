'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
SR3 - Models
'''
from gl import Renderer

r =  Renderer()
r.glInit()
r.glCreateWindow(1240,1200)
r.glViewPort(0,0,300,300)
r.glClearColor(1,0.75,0.80)
r.glColor(0.85,0.125,0.125)
r.load('./modelos/Dog.obj',[25,10],[25,25])


r.glFinish("output.bmp")