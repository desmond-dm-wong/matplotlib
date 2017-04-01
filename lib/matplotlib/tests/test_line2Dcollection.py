import matplotlib.lines as mlines
import unittest

class TestStringMethods(unittest.TestCase):

	'''
	  Test the behaviour of Line2DCollection to make sure all line2D properties 
	  are stored appropriately and used accordingly to build a particular line2D 
	  object on demand.
	'''
	def test_Line2D_default_settings(self):
		#create a line2D with default optional parameters
		col = mlines.Line2DCollection()
		#add the properties for a line2D to the collection
		col.add_line(1,[1,2,3,4], [1,4,9,16])
		#create a line2D object based on the data that was added
		#at key 1
		line = col.get_line(1)
		
		#verify all the default properties were stored accordingly
		self.assertTrue(isinstance(line,mlines.Line2D))
		self.assertEqual([1, 2, 3, 4],line.get_xdata())
		self.assertEqual([1, 4, 9, 16],line.get_ydata())
		self.assertEqual(1.5,line.get_linewidth())
		self.assertEqual('-',line.get_linestyle())
		self.assertEqual('None',line.get_marker())
		self.assertEqual('C0',line.get_color())
		self.assertEqual(6,line.get_markersize())
		self.assertTrue(line.get_antialiased())
		self.assertEqual('butt',line.get_dash_capstyle())
		self.assertEqual('round',line.get_dash_joinstyle())
		self.assertEqual('projecting',line.get_solid_capstyle())
		self.assertEqual('round',line.get_solid_joinstyle())
		self.assertEqual(5,line.get_pickradius())
		self.assertEqual('default',line.get_drawstyle())
		self.assertFalse(line.get_markevery())  

	def test_Line2D_with_linewidth(self):
		#verify the linewidth property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],0.5)
		line = col.get_line(1)
		self.assertEqual(0.5,line.get_linewidth()) 

	def test_Line2D_with_linestyle(self):
		#verify the linestyle property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],None,'--')
		line = col.get_line(1)
		self.assertEqual('--',line.get_linestyle()) 

	def test_Line2D_with_color(self):
		#verify the color property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],None,None,'#eeefff')
		line = col.get_line(1)
		self.assertEqual('#eeefff',line.get_color()) 

	def test_Line2D_with_marker(self):
		#verify the marker property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],None,None,None,"^")
		line = col.get_line(1)
		self.assertEqual('^',line.get_marker()) 

	def test_Line2D_with_markersize(self):
		#verify the markersize property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,10)
		line = col.get_line(1)
		self.assertEqual(10,line.get_markersize()) 

	def test_Line2D_with_markeredgewidth(self):
		#verify the markeredgewith property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,1.2)
		line = col.get_line(1)
		self.assertEqual(1.2,line.get_markeredgewidth()) 

	def test_Line2D_with_markeredgecolor(self):
		#verify the markeredgecolor property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,"r")
		line = col.get_line(1)
		self.assertEqual('r',line.get_markeredgecolor()) 

	def test_Line2D_with_markerfacecolor(self):
		#verify the markerfacecolor property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,"g")
		line = col.get_line(1)
		self.assertEqual('g',line.get_markerfacecolor()) 

	def test_Line2D_with_markerfacecoloralt(self):
		#verify the markerfacecoloralt property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'w')
		line = col.get_line(1)
		self.assertEqual('w',line.get_markerfacecoloralt()) 

	def test_Line2D_with_fillstyle(self):
		#verify the fillstyle property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			'right')
		line = col.get_line(1)
		self.assertEqual('right',line.get_fillstyle()) 

	def test_Line2D_with_antialiased(self):
		#verify the antialiased property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,True)
		line = col.get_line(1)
		self.assertTrue(line.get_antialiased())

	def test_Line2D_with_dash_capstyle(self):
		#verify the dash_capstyle property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,'round')
		line = col.get_line(1)
		self.assertEqual('round',line.get_dash_capstyle())

	def test_Line2D_with_solid_capstyle(self):
		#verify the solid_capstyle property was set properly
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,'butt')
		line = col.get_line(1)
		self.assertEqual('butt',line.get_solid_capstyle())

	def test_Line2D_with_dash_joinstyle(self):
		#verify the dash_joinstyle property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,None,'miter')
		line = col.get_line(1)
		self.assertEqual('miter',line.get_dash_joinstyle())

	def test_Line2D_with_solid_joinstyle(self):
		#verify the solid_joinstyle property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,None,None,'bevel')
		line = col.get_line(1)
		self.assertEqual('bevel',line.get_solid_joinstyle())

	def test_Line2D_with_pickradius(self):
		#verify the pickradius property was set properly
		
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,None,None,None,7)
		line = col.get_line(1)
		self.assertEqual(7,line.get_pickradius())

	def test_Line2D_with_drawstyle(self):
		#verify the drawstyle property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,None,None,None,None,'steps-post')
		line = col.get_line(1)
		self.assertEqual('steps-post',line.get_drawstyle())

	def test_Line2D_with_markevery(self):
		#verify the markevery property was set properly
	
		col = mlines.Line2DCollection()
		col.add_line(1,[1,2,3,4], [1,4,9,16],
			None,None,None,None,None,None,None,None,'none',
			None,None,None,None,None,None,None,None,True)
		line = col.get_line(1)
		self.assertTrue(line.get_markevery())

	def test_multiple_Line2D_with_settings(self):
		#verify the settings are stored appropriately for multiple lines
	
		col = mlines.Line2DCollection()
		#add line 1 settings
		col.add_line(1,[1,2,3,4], [1,2,3,4],
			0.6,'dashed',None,None,None,None,None,None,'none',
			None,None,None,None,None,None,3,None,False)
		#add line 2 settings
		col.add_line(2,[1,2,3,4], [1,4,9,16],
			0.1,'dashdot',None,None,None,None,None,None,'none',
			None,None,None,None,None,None,6,None,True)
		line1 = col.get_line(1)
		line2 = col.get_line(2)
		
		#check the properties for line1
		self.assertEqual([1, 2, 3, 4],line1.get_xdata())
		self.assertEqual([1, 2, 3, 4],line1.get_ydata())
		self.assertEqual(0.6,line1.get_linewidth())
		self.assertEqual('--',line1.get_linestyle())
		self.assertEqual(3,line1.get_pickradius())
		self.assertFalse(line1.get_markevery())
		
		#check the properties for line2
		self.assertEqual([1, 2, 3, 4],line2.get_xdata())
		self.assertEqual([1, 4, 9, 16],line2.get_ydata())
		self.assertEqual(0.1,line2.get_linewidth())
		self.assertEqual('-.',line2.get_linestyle())
		self.assertEqual(6,line2.get_pickradius())
		self.assertTrue(line2.get_markevery())

if __name__ == '__main__':
    unittest.main()