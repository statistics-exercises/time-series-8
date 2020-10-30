import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "you have plotted the wrong number of coordinates in your graph" )
        for i in range(len(this_y)) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates of the points in your graph are incorrect" )
            bar = np.sqrt(lamd*time/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( this_y[i] - lamd*time )<bar, "the y-coordinates of the points in your graph appear to  be incorrect" )
  
   def test_expectation(self) : 
       self.assertTrue( np.abs( expectation - lamd*time ) < 1e-7, "the value you have set for the variable expectation is incorrect"  )
