#!/usr/bin/env python
# -*- Python -*-

"""
 \file HiroNXGUI.py
 \brief HiroNX GUI
 \date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import _GlobalIDL, _GlobalIDL__POA

# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
hironxgui_spec = ["implementation_id", "HiroNXGUI", 
		 "type_name",		 "HiroNXGUI", 
		 "description",	   "HiroNX GUI", 
		 "version",		   "1.0.0", 
		 "vendor",			"AIST", 
		 "category",		  "VMRG", 
		 "activity_type",	 "STATIC", 
		 "max_instance",	  "1", 
		 "language",		  "Python", 
		 "lang_type",		 "SCRIPT",
		 ""]
# </rtc-template>

class HiroNXGUI(OpenRTM_aist.DataFlowComponentBase):
	def SetApp(self, app):
		self._app = app
		 
	
	"""
	\class HiroNXGUI
	\brief HiroNX GUI
	
	"""
	def __init__(self, manager):
		"""
		\brief constructor
		\param manager Maneger Object
		"""
		print 'gen HiroNXGUI'
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)


		"""
		"""
		self._HiroNXPort = OpenRTM_aist.CorbaPort("HiroNX")
		"""
		"""
		self._HIROPort = OpenRTM_aist.CorbaPort("HIRO")

		

		"""
		"""
		self._manipulator = OpenRTM_aist.CorbaConsumer(interfaceType=_GlobalIDL.HiroNX)
		"""
		"""
		self._common = OpenRTM_aist.CorbaConsumer(interfaceType=_GlobalIDL.CommonCommands)
		"""
		"""
		self._motion = OpenRTM_aist.CorbaConsumer(interfaceType=_GlobalIDL.MotionCommands)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>
		self._app = None

	def onInitialize(self):
		"""
		
		The initialize action (on CREATED->ALIVE transition)
		formaer rtc_init_entry() 
		
		\return RTC::ReturnCode_t
		
		"""
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		self._HiroNXPort.registerConsumer("manipulator", "HiroNX", self._manipulator)
		self._HIROPort.registerConsumer("common", "CommonCommands", self._common)
		self._HIROPort.registerConsumer("motion", "MotionCommands", self._motion)
		
		# Set CORBA Service Ports
		self.addPort(self._HiroNXPort)
		self.addPort(self._HIROPort)
		
		return RTC.RTC_OK
	
	#def onFinalize(self, ec_id):
	#	"""
	#
	#	The finalize action (on ALIVE->END transition)
	#	formaer rtc_exiting_entry()
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onStartup(self, ec_id):
	#	"""
	#
	#	The startup action when ExecutionContext startup
	#	former rtc_starting_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK

	def onShutdown(self, ec_id):
		"""
		
		The shutdown action when ExecutionContext stop
		former rtc_stopping_entry()
		
		\param ec_id target ExecutionContext Id
		
		\return RTC::ReturnCode_t
		
		"""
		print 'Going Shutdown... Please wait a minute.'
		if self._app:
			self._app.frame.Close()
		
		return RTC.RTC_OK
	
	def onActivated(self, ec_id):
		"""
	
		The activated action (Active state entry action)
		former rtc_active_entry()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		if self._app:
			self._app.Activate()
		else:
			print 'app none'
		return RTC.RTC_OK
	
	def onDeactivated(self, ec_id):
		"""
	
		The deactivated action (Active state exit action)
		former rtc_active_exit()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		if self._app:
			self._app.Deactivate()
	
		return RTC.RTC_OK
	
	#def onExecute(self, ec_id):
	#	"""
	#
	#	The execution action that is invoked periodically
	#	former rtc_active_do()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onAborting(self, ec_id):
	#	"""
	#
	#	The aborting action when main logic error occurred.
	#	former rtc_aborting_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onError(self, ec_id):
	#	"""
	#
	#	The error action in ERROR state
	#	former rtc_error_do()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onReset(self, ec_id):
	#	"""
	#
	#	The reset action that is invoked resetting
	#	This is same but different the former rtc_init_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onStateUpdate(self, ec_id):
	#	"""
	#
	#	The state update action that is invoked after onExecute() action
	#	no corresponding operation exists in OpenRTm-aist-0.2.0
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onRateChanged(self, ec_id):
	#	"""
	#
	#	The action that is invoked when execution context's rate is changed
	#	no corresponding operation exists in OpenRTm-aist-0.2.0
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	



def HiroNXGUIInit(manager):
	profile = OpenRTM_aist.Properties(defaults_str=hironxgui_spec)
	manager.registerFactory(profile,
							HiroNXGUI,
							OpenRTM_aist.Delete)

def MyModuleInit(manager):
	HiroNXGUIInit(manager)

	# Create a component
	comp = manager.createComponent("HiroNXGUI")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
