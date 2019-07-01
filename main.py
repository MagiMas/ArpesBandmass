from fitMasses import FitClass
import fitfunctions as ffs
import numpy as np
import matplotlib.pyplot as plt
import Basefile as Bf
from DataFittingWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

with open('Last_Directory.txt', 'r') as f:
    plt.rcParams["savefig.directory"] = f.readline()
    f.close()

class UpdateDirectoryFile(QtCore.QThread):
    #sig1 = QtCore.pyqtSignal(str)
    def __init__(self, lineftxt, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.source_txt = lineftxt

    def run(self):
        f = open('Last_Directory.txt', 'w')
        f.write(self.source_txt)
        f.close()
        plt.rcParams['savefig.directory'] = self.source_txt
        #self.sig1.emit(self.source_txt)

class ARPESMassApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.hbar = 6.582e-16
        self.me = 9.11e-31

        # update Plots
        self.WDGT_ARPES.canvas.ax.set_xlabel(r'Wavevector [$\mathrm{\AA^{-1}}$]')
        self.WDGT_ARPES.canvas.ax.set_ylabel('Energy [eV]')
        self.WDGT_Profile.canvas.ax.set_xlabel(r'Wavevector [$\mathrm{\AA^{-1}}$]')
        self.WDGT_Profile.canvas.ax.set_ylabel('Intensity [a.u.]')

        # Manage Radio Button for MDC or EDC mode
        self.MODE = 'MDC' # 'MDC' or 'EDC'
        self.RB_Mode_MDC.setChecked(True)
        self.RB_Mode_MDC.toggled.connect(lambda:self.changeMode("MDC"))
        self.RB_Mode_EDC.toggled.connect(lambda:self.changeMode("EDC"))
        self.RB_Mode_Free.toggled.connect(lambda:self.changeMode("Free"))

        # Manage Editing for MDC and EDC
        self.EDITING_ARPES = False
        self.PB_DC_Editing.released.connect(self.changeEditingArpes)

        # Manage Radio Button for Linear or Quadratic Band Fit
        self.BANDFIT_DICT = ffs.fitfunc_dict['quad']
        self.BANDFIT = 'quad' # 'quad' or 'linear'
        self.RB_Fit_Quadratic.setChecked(True)
        self.RB_Fit_Quadratic.toggled.connect(lambda:self.changeBandfit("quad"))
        self.RB_Fit_Linear.toggled.connect(lambda:self.changeBandfit("linear"))
        self.RB_Fit_Mexican.toggled.connect(lambda:self.changeBandfit("mexican"))


        # Manage Editing for Profile
        self.EDITING_PROFILE = True
        self.PB_Profile_Editing.released.connect(self.changeEditingProfile)
        self.PB_Profile_Editing.setText('Disable Editing')

        # Manage LineEdit for Input of Starting Fit Parameters for Bandfit
        self.LE_Update_Bandfit.setText(', '.join(str(e) for e in self.BANDFIT_DICT['start_parameters']))
        self.LBL_Fitfunc.setText('\t' + self.BANDFIT_DICT['function_template'])

        # Manage Pushbutton to update Fit Parameters for Bandfit
        self.PB_Update_Bandfit.released.connect(self.updateBandFit_parameters)

        # Manage Radio Button for Lorentzian or Gaussian EDC/MDC Fit
        self.DCFIT_DICT = ffs.fitfunc_dict['lorentz']
        self.DCFIT = 'lorentz'
        self.RB_Lorentzian.setChecked(True)
        self.RB_Lorentzian.toggled.connect(lambda:self.changeDCFit('lorentz'))
        self.RB_Gaussian.toggled.connect(lambda:self.changeDCFit('gauss'))

        # Manage LineEdit for Input of Starting Fit Parameters for EDC/MDC Fit
        self.LE_Parameters.setText(', '.join(str(e) for e in self.DCFIT_DICT['start_parameters']))
        self.LBL_Parameters.setText(self.DCFIT_DICT['function_template'])

        # Manage Pushbutton to update Fit parameters for EDC/MDC Fit
        self.PB_Update.released.connect(self.updateDCFit_parameters)

        # Manage File Loading
        f_ = open('Last_Directory.txt', 'r')
        self.DIR = f_.readline()
        f_.close()
        self.LE_Dir.setText(self.DIR)
        self.PB_Dir.released.connect(self.chooseDir)
        self.PB_Dir_Load.released.connect(self.loadDir)
        self.PB_File.released.connect(self.loadARPES)

        # Manage ARPES FIGURE
        self.ARPES_Dict = {
            'line' : None,
            'lineval' : None,
            'linetype' : None,
            'linevalsFree' : [[], []],
            'scatterpoints' : [],
            'scatterpointsPlot' : None,
            'fitplot' : None
        }
        self.WDGT_ARPES.canvas.mpl_connect('button_press_event', self.onclickArpes)

        # Manage Profile Figure
        self.Profile_Dict = {
            'lineLeft' : None,
            'lineLeftval' : None,
            'lineRight' : None,
            'lineRightval' : None,
            'dataX' : None,
            'dataY' : None,
            'fitdataX' : None,
            'fitdataY' : None,
            'linePlot' : None,
            'fitPlot' : None,
            'peakX' : None,
            'peakY' : None,
            'peakScatter' : None
        }
        self.WDGT_Profile.canvas.mpl_connect('button_press_event', self.onclickProfile)

        # Add Fit Point from Profile to ARPES Graph
        self.PB_P2A.released.connect(self.addFitPointARPES)

        # Manage Fitting ARPES
        self.PB_Fit_ARPES.released.connect(self.fitARPES)

        # Manage Fitting Profile
        self.PB_FitProf.released.connect(self.fitProfile)
        self.ChB_Estimate_Params_Profile.setChecked(True)
        self.EstimateProfileParams = self.ChB_Estimate_Params_Profile.isChecked()
        self.ChB_Estimate_Params_Profile.stateChanged.connect(self.EstimateFitParamsProfileBool)

    # Manage the Estimation of the Profile Parameters
    def EstimateFitParamsProfile(self):
        if self.Profile_Dict['lineLeft'] and self.Profile_Dict['lineRight']:
            xdata = np.linspace(self.Profile_Dict['lineLeftval'], self.Profile_Dict['lineRightval'], 200)
            ydata = self.Spec1D.IDATA(xdata)
            intensity = np.amax(ydata)
            x0 = 0.5*(self.Profile_Dict['lineRightval'] - self.Profile_Dict['lineLeftval'])
            if self.Profile_Dict['lineRightval'] > self.Profile_Dict['lineRightval']:
                x0 = self.Profile_Dict['lineLeftval'] - 0.5*(self.Profile_Dict['lineRightval'] - self.Profile_Dict['lineLeftval']) 
            else:
                x0 = self.Profile_Dict['lineLeftval'] + 0.5*(self.Profile_Dict['lineRightval'] - self.Profile_Dict['lineLeftval']) 
            constBkg = np.amin(ydata)
            broadening = 0.33*np.abs(self.Profile_Dict['lineRightval'] - self.Profile_Dict['lineLeftval'])
            params = self.DCFIT_DICT['start_parameters']
            intensity -= constBkg
            try:
                i_intensity = self.DCFIT_DICT['parameter_names'].index('intensity')
                params[i_intensity] = intensity
            except:
                print('no intensity parameter found')
            try:
                i_broadening = self.DCFIT_DICT['parameter_names'].index('broadening')
                params[i_broadening] = broadening
            except:
                print("No broadening parameter found")
            try:
                i_x0 = self.DCFIT_DICT['parameter_names'].index('x0')
                params[i_x0] = x0
            except:
                print("No x0 parameter found")
            try:
                i_constBkg = self.DCFIT_DICT['parameter_names'].index('const_background')
                params[i_constBkg] = constBkg
            except:
                print("No const_background parameter found")

            self.DCFIT_DICT['start_parameters'] = params
            print("Estimated parameters: ", params)
            self.LE_Parameters.setText(', '.join("%.1E" % e for e in self.DCFIT_DICT['start_parameters']))
        else:
            print("Please define left and right border")

    def EstimateFitParamsProfileBool(self):
        self.EstimateProfileParams = self.ChB_Estimate_Params_Profile.isChecked()

    # Manage the fitting in the Profile Plot
    def fitProfile(self):
        if not self.Profile_Dict['lineLeft'] or not self.Profile_Dict['lineRight']:
            print("Please give left and right border of fit")
        else:
            xfit = np.linspace(self.Profile_Dict['lineLeftval'], self.Profile_Dict['lineRightval'], 200)
            try:
                if self.Profile_Dict['fitPlot']:
                    self.Profile_Dict['fitPlot'].remove()
                self.Profile_Dict['fitPlot'] = None
                ydata = self.Spec1D.IDATA(xfit)
                fitting = FitClass(xfit, ydata, self.DCFIT_DICT)
                if self.EstimateProfileParams:
                    params = fitting.estimate_start_parameters()
                    self.DCFIT_DICT['start_parameters'] = params
                    print("Estimated parameters: ", params)
                    self.LE_Parameters.setText(', '.join("%.1E" % e for e in self.DCFIT_DICT['start_parameters']))
                fitting.do_fit()
                yfit = fitting.fitcurve(xfit)
                self.Profile_Dict['fitPlot'], = self.WDGT_Profile.canvas.ax.plot(xfit, yfit, color='k')

                i_x0 = self.DCFIT_DICT['parameter_names'].index('x0')
                peakX = fitting.POPT[i_x0]
                peakY = fitting.fitcurve([peakX])

                if self.Profile_Dict['peakScatter']:
                    self.Profile_Dict['peakScatter'].remove()
                self.Profile_Dict['peakX'] = peakX
                self.Profile_Dict['peakY'] = peakY
                self.Profile_Dict['peakScatter'] = self.WDGT_Profile.canvas.ax.scatter(peakX, peakY, color='#c65411')

                output = ''
                i = 0
                for element in fitting.POPT:
                    output += 'a%d = ' % i + str(element) + '\n'
                    i += 1
                self.TE_ARPES_output.setText(output)
            except:
                print("couldn't fit Profile")
            self.WDGT_Profile.canvas.draw_idle()

    # manage the fitting in ARPES window
    def fitARPES(self):
        if not self.ARPES_Dict['scatterpoints']:
            print("No data to fit to")
        else:
            if self.ARPES_Dict['fitplot']:
                self.ARPES_Dict['fitplot'].remove()
            self.ARPES_Dict['fitplot'] = None
            xdat, ydat = [], []
            for point in self.ARPES_Dict['scatterpoints']:
                xdat.append(point[0])
                ydat.append(point[1])
            #print(self.BANDFIT_DICT['start_parameters'])
            fitting = FitClass(xdat, ydat, self.BANDFIT_DICT)
            try:
                fitting.do_fit()
            except:
                print("Fitting not succesful")
                p_ = self.BANDFIT_DICT['start_parameters']
                self.ARPES_Dict['fitplot'], = self.WDGT_ARPES.canvas.ax.plot(xdat, [self.BANDFIT_DICT['function'](x, *p_) for x in xdat], color='#c65411')
            xstart, xstop = np.amin(xdat), np.amax(xdat)
            xDelta = xstop - xstart
            xfit = np.linspace(xstart-xDelta*0.05, xstop+xDelta*0.05, 200)
            try:
                yfit = fitting.fitcurve(xfit)
                self.ARPES_Dict['fitplot'], = self.WDGT_ARPES.canvas.ax.plot(xfit, yfit, color='#c65411')
                output = ''
                i = 0
                for element in fitting.POPT:
                    output += 'a%d = ' % i + str(element) + '\n'
                    i += 1
                if self.BANDFIT == "quad":
                    output += "m* = %f m_e" % self.calculateEffectiveMassQuadratic(fitting.POPT[0])
                self.TE_ARPES_output.setText(output)
            except:
                print("fitting.fitcurve problem")
            self.WDGT_ARPES.canvas.draw_idle()

    # Convert fit parameter a0 into effective mass in units of electron mass
    def calculateEffectiveMassQuadratic(self, parameter):
        factor = self.hbar**2 * 16.021766 / (2.*self.me)
        return factor/parameter
    
    # plot the points used for fitting
    def plotFitPointsARPES(self):
        if self.ARPES_Dict['scatterpointsPlot']:
            self.ARPES_Dict['scatterpointsPlot'].remove()
        xvals = []
        yvals = []
        for point in self.ARPES_Dict['scatterpoints']:
            xvals.append(point[0])
            yvals.append(point[1])
        self.ARPES_Dict['scatterpointsPlot'] = self.WDGT_ARPES.canvas.ax.scatter(xvals, yvals, color='#c65411')
        self.WDGT_ARPES.canvas.draw()

    # add a fitpoint according to positions
    def addFitPointARPES(self):
        try:
            if self.MODE == "Free":
                x = self.Profile_Dict['peakX']
                start, stop = self.ARPES_Dict['linevalsFree']
                px, py = np.array(start) + x * (np.array(stop) - np.array(start))/np.linalg.norm((np.array(stop) - np.array(start)))
                self.ARPES_Dict['scatterpoints'].append((px,py))
            else:
                px, py = self.Profile_Dict['peakX'], self.ARPES_Dict['lineval']
                if px and py:
                    if self.MODE == "MDC":
                        self.ARPES_Dict['scatterpoints'].append((px,py))
                    else:
                        self.ARPES_Dict['scatterpoints'].append((py,px))
                else:
                    print("no real fitpoint")
            self.plotFitPointsARPES()
        except:
            print("Couldn't add fitpoint")

    # clear the profile graph
    def clearProfileGraph(self):
        if self.Profile_Dict['linePlot']:
            self.Profile_Dict['linePlot'].remove()
        if self.Profile_Dict['fitPlot']:
            self.Profile_Dict['fitPlot'].remove()
        if self.Profile_Dict['peakScatter']:
            self.Profile_Dict['peakScatter'].remove()
        if self.Profile_Dict['lineLeft']:
            self.Profile_Dict['lineLeft'].remove()
        if self.Profile_Dict['lineRight']:
            self.Profile_Dict['lineRight'].remove()
        self.Profile_Dict['linePlot'] = None
        self.Profile_Dict['fitPlot'] = None
        self.Profile_Dict['dataX'] = None
        self.Profile_Dict['dataY'] = None
        self.Profile_Dict['fitdataX'] = None
        self.Profile_Dict['fitdataY'] = None
        self.Profile_Dict['peakScatter'] = None
        self.Profile_Dict['peakX'] = None
        self.Profile_Dict['peakY'] = None
        self.Profile_Dict['lineLeft'] = None
        self.Profile_Dict['lineLeftval'] = None
        self.Profile_Dict['lineRight'] = None
        self.Profile_Dict['lineRightval'] = None

    # Manage the Interactive elements of the Profile Graph
    def onclickProfile(self,event):
        if self.EDITING_PROFILE and event.xdata and event.ydata:
            # manually add scatterpoint
            if event.button == 2:
                try:
                    if self.Profile_Dict['peakScatter']:
                        self.Profile_Dict['peakScatter'].remove()
                    ypoint = self.Spec1D.IDATA(event.xdata)
                    self.Profile_Dict['peakX'] = event.xdata
                    self.Profile_Dict['peakY'] = ypoint
                    self.Profile_Dict['peakScatter'] = self.WDGT_Profile.canvas.ax.scatter(event.xdata, ypoint, color='#c65411')
                    
                except:
                    print("No Spec1D object")
                    raise
            # add left border for fit
            if event.button == 1:
                if self.Profile_Dict['lineLeft']:
                    self.Profile_Dict['lineLeft'].remove()
                    self.Profile_Dict['lineLeftval'] = None
                self.Profile_Dict['lineLeft'] = self.WDGT_Profile.canvas.ax.axvline(event.xdata, color='#41701c')
                self.Profile_Dict['lineLeftval'] = event.xdata
                # if self.EstimateProfileParams:
                #     self.EstimateFitParamsProfile()
            # add right border for fit
            if event.button == 3:
                if self.Profile_Dict['lineRight']:
                    self.Profile_Dict['lineRight'].remove()
                    self.Profile_Dict['lineRightval'] = None
                self.Profile_Dict['lineRight'] = self.WDGT_Profile.canvas.ax.axvline(event.xdata, color='#601c70')
                self.Profile_Dict['lineRightval'] = event.xdata
                # if self.EstimateProfileParams:
                #     self.EstimateFitParamsProfile()
            self.WDGT_Profile.canvas.draw()
                

    # handle the redrawing of vlines, hlines, cutting data etc.
    def onclickArpes(self, event):
        if self.EDITING_ARPES and event.xdata and event.ydata:
            # take horizontal/vertical cut for Profile with left mouse button
            if self.MODE == "Free":
                if event.button == 1:
                    if self.ARPES_Dict['line']:
                        self.ARPES_Dict['line'].remove()
                        self.ARPES_Dict['linetype'] = "Free"
                        self.ARPES_Dict['lineval'] = None
                        self.ARPES_Dict['line'] = None
                    self.ARPES_Dict['linevalsFree'][0] = [event.xdata, event.ydata]
                elif event.button == 3:
                    if self.ARPES_Dict['line']:
                        self.ARPES_Dict['line'].remove()
                        self.ARPES_Dict['linetype'] = "Free"
                        self.ARPES_Dict['lineval'] = None
                        self.ARPES_Dict['line'] = None
                    self.ARPES_Dict['linevalsFree'][1] = [event.xdata, event.ydata]
                # remove scatterpoints with middle mouse click
                elif event.button == 2:
                    if self.ARPES_Dict['scatterpoints']:
                        dist_threshold = 0.1
                        distances = []
                        for point in self.ARPES_Dict['scatterpoints']:
                            dist = np.sqrt((event.xdata - point[0])**2 + (event.ydata - point[1])**2)
                            distances.append(dist)
                        
                        mindist = min(distances)
                        mindist_i = distances.index(min(distances))
                        if mindist < dist_threshold:
                            self.ARPES_Dict['scatterpoints'].pop(mindist_i)
                            self.plotFitPointsARPES()
                try:
                    start, stop = self.ARPES_Dict['linevalsFree']
                    if event.button != 2:
                        self.ARPES_Dict['line'], = self.WDGT_ARPES.canvas.ax.plot([start[0], stop[0]], [start[1], stop[1]], color='k')
                    self.clearProfileGraph()
                    #self.WDGT_Profile.canvas.ax.relim()
                    tx,ty = self.Spec.lineprofileFree(start, stop, 200)
                    self.Spec1D = Bf.Spectra1D(tx, ty)
                    self.Profile_Dict['dataX'] = tx
                    self.Profile_Dict['dataY'] = ty
                    self.Profile_Dict['linePlot'], = self.WDGT_Profile.canvas.ax.plot(tx, ty, color='#1165c6')
                    self.WDGT_Profile.canvas.ax.set_xlim(np.amin(tx)-0.05*np.abs(np.amin(tx) - np.amax(tx)), np.amax(tx)+0.05*np.abs(np.amin(tx) - np.amax(tx)))
                    self.WDGT_Profile.canvas.ax.set_ylim(np.amin(ty)-0.05*np.abs(np.amin(ty) - np.amax(ty)), np.amax(ty)+0.05*np.abs(np.amin(ty) - np.amax(ty)))
                except:
                    print("Couldn't load Spectra object")
                self.WDGT_ARPES.canvas.draw()
                self.WDGT_Profile.canvas.draw()
            else:
                if event.button == 1:
                    if self.ARPES_Dict['line']:
                        self.ARPES_Dict['line'].remove()
                        self.ARPES_Dict['linetype'] = None
                        self.ARPES_Dict['lineval'] = None
                    dim = "a"
                    val = 0.
                    if self.MODE == "EDC":
                        self.ARPES_Dict['line'] = self.WDGT_ARPES.canvas.ax.axvline(event.xdata, color='k')
                        self.ARPES_Dict['linetype'] = 'EDC'
                        self.ARPES_Dict['lineval'] = event.xdata
                        val = event.xdata
                        dim = "y"
                    elif self.MODE == "MDC":
                        self.ARPES_Dict['line'] = self.WDGT_ARPES.canvas.ax.axhline(event.ydata, color='k')
                        self.ARPES_Dict['linetype'] = 'MDC'
                        self.ARPES_Dict['lineval'] = event.ydata
                        val = event.ydata
                        dim = "x"
                    try:
                        self.clearProfileGraph()
                        #self.WDGT_Profile.canvas.ax.relim()
                        tx,ty = self.Spec.lineprofileXY(dim=dim, val=val)
                        self.Spec1D = Bf.Spectra1D(tx, ty)
                        self.Profile_Dict['dataX'] = tx
                        self.Profile_Dict['dataY'] = ty
                        self.Profile_Dict['linePlot'], = self.WDGT_Profile.canvas.ax.plot(tx, ty, color='#1165c6')
                        self.WDGT_Profile.canvas.ax.set_xlim(np.amin(tx)-0.05*np.abs(np.amin(tx) - np.amax(tx)), np.amax(tx)+0.05*np.abs(np.amin(tx) - np.amax(tx)))
                        self.WDGT_Profile.canvas.ax.set_ylim(np.amin(ty)-0.05*np.abs(np.amin(ty) - np.amax(ty)), np.amax(ty)+0.05*np.abs(np.amin(ty) - np.amax(ty)))
                    except:
                        print("Couldn't load Spectra object")
                    self.WDGT_ARPES.canvas.draw()
                    self.WDGT_Profile.canvas.draw()
                # add scatterpoint with right mouse button
                elif event.button == 3:
                    try:
                        px, py = event.xdata, event.ydata
                        self.ARPES_Dict['scatterpoints'].append((px,py))
                        self.plotFitPointsARPES()
                    except:
                        print("Couldn't add fitpoint")
                
                # remove scatterpoints with middle mouse click
                elif event.button == 2:
                    if self.ARPES_Dict['scatterpoints']:
                        dist_threshold = 0.1
                        distances = []
                        for point in self.ARPES_Dict['scatterpoints']:
                            dist = np.sqrt((event.xdata - point[0])**2 + (event.ydata - point[1])**2)
                            distances.append(dist)
                        
                        mindist = min(distances)
                        mindist_i = distances.index(min(distances))
                        if mindist < dist_threshold:
                            self.ARPES_Dict['scatterpoints'].pop(mindist_i)
                            self.plotFitPointsARPES()


    # load actual file, put it into a Spectra class and plot on ARPES ax
    def loadARPES(self):
        try:
            if self.ARPES_Dict['scatterpointsPlot']:
                self.ARPES_Dict['scatterpointsPlot'].remove()
            self.ARPES_Dict['scatterpointsPlot'] = None
            self.ARPES_Dict['scatterpoints'] = []
            if self.ARPES_Dict['fitplot']:
                self.ARPES_Dict['fitplot'].remove()
            self.ARPES_Dict['fitplot'] = None
            if self.EDITING_ARPES:
                self.changeEditingArpes()
            self.Spec = Bf.load_a_spectrum(os.path.join(self.DIR, self.CB_Files.currentText()))
            self.Spec.plot_data_on_ax(self.WDGT_ARPES.canvas.ax, plot=False)
            self.WDGT_ARPES.canvas.draw_idle()
            self.WDGT_ARPES.toolbar.update()
        except:
            print("Something went wrong with loading the Spectrum!")

    # choose directory via filedialog
    def chooseDir(self):
        working_dir = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory",self.DIR))
        
        tempThread = UpdateDirectoryFile(working_dir)
        tempThread.start()
        tempThread.requestInterruption()
        tempThread.wait()

        self.LE_Dir.setText(working_dir)
        self.DIR = working_dir

    # load contents in directory into combobox
    def loadDir(self):
        self.CB_Files.clear()
        self.CB_Files.addItems([f for f in os.listdir(self.DIR) if os.path.isfile(os.path.join(self.DIR, f))])

    # change if Editing of Contents in ARPES Plot is allowed
    def changeEditingArpes(self):
        self.EDITING_ARPES = not self.EDITING_ARPES
        if self.EDITING_ARPES:
            print("Editing enabled")
            self.PB_DC_Editing.setText('Disable Editing')
        else:
            print("Editing disabled")
            if self.ARPES_Dict['line']:
                self.ARPES_Dict['line'].remove()
            self.ARPES_Dict['line'] = None

            self.clearProfileGraph()
            self.WDGT_ARPES.canvas.draw_idle()
            self.WDGT_Profile.canvas.draw_idle()
            self.PB_DC_Editing.setText('Enable Editing')

    # change if Editing of Contents in Profile Plot is allowed
    def changeEditingProfile(self):
        self.EDITING_PROFILE = not self.EDITING_PROFILE
        if self.EDITING_PROFILE:
            print("Editing Profile enabled")
            self.PB_Profile_Editing.setText('Disable Editing')
        else:
            print("Editing Profile disabled")
            self.PB_Profile_Editing.setText('Enable Editing')

    # change between MDC, EDC and Free mode for individual curves, update figures accordingly
    def changeMode(self, button):
        self.MODE = button
        if button == "MDC":
            self.WDGT_Profile.canvas.ax.set_xlabel(r'Wavevector [$\mathrm{\AA^{-1}}$]')
        elif button == "EDC":
            self.WDGT_Profile.canvas.ax.set_xlabel(r'Energy [eV]')
        elif button == "Free":
            print("Free")
            self.WDGT_Profile.canvas.ax.set_xlabel(r'')
            if self.ARPES_Dict['line']:
                self.ARPES_Dict['line'].remove()
            self.ARPES_Dict['line'] = None

            self.clearProfileGraph()
            self.WDGT_ARPES.canvas.draw_idle()
            self.WDGT_Profile.canvas.draw_idle()
        self.WDGT_Profile.canvas.draw()

    # change between linear and quadratic bandfit
    def changeBandfit(self, button):
        self.BANDFIT = button
        self.BANDFIT_DICT = ffs.fitfunc_dict[button]
        self.LE_Update_Bandfit.setText(', '.join(str(e) for e in self.BANDFIT_DICT['start_parameters']))
        self.LBL_Fitfunc.setText('\t' + self.BANDFIT_DICT['function_template'])

    # update bandfit parameters
    def updateBandFit_parameters(self):
        params = self.LE_Update_Bandfit.text()
        try:
            values = [float(p) for p in params.split(',')]
        except:
            print("couldn't convert to float")
            return
        if len(values) == len(self.BANDFIT_DICT['start_parameters']):
            self.BANDFIT_DICT['start_parameters'] = values
            print("updated bandfit to", values)
        else:
            print("Couldn't update to ", values)

    # change between lorentz and gauss fit
    def changeDCFit(self, button):
        self.DCFIT = button
        self.DCFIT_DICT = ffs.fitfunc_dict[button]
        self.LBL_Parameters.setText(self.DCFIT_DICT['function_template'])

    # update fit parameters for EDC/MDC fits
    def updateDCFit_parameters(self):
        params = self.LE_Parameters.text()
        try:
            values = [float(p) for p in params.split(',')]
        except:
            print("couldn't convert to float")
            return
        if len(values) == len(self.DCFIT_DICT['start_parameters']):
            self.DCFIT_DICT['start_parameters'] = values
            print("updated EDC/MDC fit to", values)
        else:
            print("Couldn't update to ", values)



def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("plastique")
    form = ARPESMassApp()
    form.show()
    app.exec_()




if __name__ == '__main__':
    main()