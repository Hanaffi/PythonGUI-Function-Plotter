from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import  numpy  as  np 
from sympy import lambdify
from sympy.abc import x

from PyQt5.QtCore import Qt 


class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        
        QMainWindow . __init__ ( self )

        loadUi ( "test.ui" , self ) #loading the UI

        self . setWindowTitle ( "Task 0" ) #Setting the title
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setStyleSheet("""QMainWindow{border: 1px solid #093038;}""") 

        self . plot_button . clicked . connect ( self . PLOT )
        self.btn_close.clicked.connect(self.close) #Handling clicking close button
        self.btn_minimize.clicked.connect(self.showMinimized) #Handling clicking minimize button
        
        #Toolbar
        self.toolbar = self . addToolBar ( NavigationToolbar ( self . MplWidget . canvas ,  self ))
        

    def  PLOT ( self ):
        try:#Checking if the input x values are numbers
            val_from = float(self.from_x.text())
            val_to = float(self.to_x_2.text())
            self.error_place.setText("")
            try:#Checking if the input function is valid
                fun=self.y_of_x.text()
                f = lambdify(x,fun )
                if val_from>val_to: #Swap values if start > end
                    val_from , val_to = val_to , val_from
                
                #Generating x values
                x_range  =  np . linspace ( val_from , val_to , 100000 )
                #Generating y values
                y_range=np.asarray([f(x) for x in x_range])
                
                #Setting the canvas
                self . MplWidget . canvas . axes . clear () 
                self . MplWidget . canvas . axes . plot ( x_range ,  y_range ) 
                self . MplWidget . canvas . axes . legend (( 'y' ,  'x' ),loc = 'upper right' ) 
                self . MplWidget . canvas . axes . set_title ( ' y(x)' ) 
                self . MplWidget . canvas . draw ()
            except SyntaxError:
                self.error_place.setText("Invalid function format!")
            except NameError:
                self.error_place.setText("Invalid function format!")
            except ValueError:   
                self.error_place.setText("Invalid function format!")
        except ValueError:   
            self.error_place.setText("x values must be numbers")
        except SyntaxError:
            self.error_place.setText("x values must be numbers")
        except NameError:
            self.error_place.setText("x values must be numbers")
        
        
        
#Exporting the starting function to runner.py
def START():        
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    window  =  MatplotlibWidget () 
    window . show () 
    app . exec_ ()
    

# Start 
# START()