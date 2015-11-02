Title: Fabric's behaviour for booleans is non-obvious
Date: 2015-11-02 15:30
Category: coding


	:::python
	def get_latest(no_download=False):
	    return bool(no_download)
  ##################################
  $ fab get_latest                 
  False
  $ fab get_latest:no_download     
  True
  $ fab get_latest:no_download=False     
  True
  
Everything passed in to fabric is a string, so be aware that `bool("0") == True` and `bool("False") == True`.

Bools are a special case, make sure they default to false and you'll get nice behavior. There seems to be no way to make bool args default to True, and then be overridden by False in code.
