# *-* coding:utf-8 *-*
import json
import sys
import qrcode
import base64

class ShadowSocks():
	def __init__(self, filename):
		self.filename = filename
		self.server = ''
		self.server_port = ''
		self.method = ''
		self.password = ''

	def checkfile(self):
		try:
			fp = open(self.filename)
			data = json.load(fp)
			self.server = data['server']
			self.server_port = data['server_port']
			self.method = data['method']
			self.password = data['password']
			fp.close()
		except:
			print "文件出错"
			raise
	def generation(self):
		ssurl = '%s:%s@%s:%s' % (self.method, \
			self.password, \
			self.server, \
			self.server_port
			)
		ssurl = 'ss://' + base64.encodestring(ssurl)
		img = qrcode.make(ssurl)
		img.show()

if len(sys.argv) == 2:
	ss = ShadowSocks(sys.argv[1])
	ss.checkfile()
	ss.generation()
else:
	print "参数出错"