#!/usr/bin/env python3
#-*-coding : utf-8 -*-
import os
import sys
import time

"""
源码地址：
需要配置如下信息
"""
# 项目路径(末尾不带/)
project_path = "~/Desktop/DEN"
# 项目名称
project_name = "DENFramework"
# 填 xcworkspace 或 xcodeproj
project_suffix = "xcworkspace"
# 填 Release 或 Debug
config = "Release"
# 如果没有建其他target那就是和项目名是一样的
target_name = "DENFramework"
# 导出路径
export_path  = "~/Desktop"
# exportPlist.plist的路径
option_plist_path = "~/Download/auto_packing/exportOptions.plist"
# 上传服务器地址(没有的话填空 不上传)
server_address = ""

def clean():
	print('## - clean - ##')
	os.system('cd %s;xcodebuild clean' % project_path)

def	build_archive():
	print('## - build - ##')
	exi = os.path.exists("%s/build" % project_path)
	if exi == False:
		os.system('cd %s;mkdir build' % project_path)
	os.system ('cd %s;xcodebuild archive %s %s.%s -scheme %s -configuration %s -archivePath %s/build/%s || exit' % (project_path, project_suffix, project_name, project_suffix, target_name, config, project_path, project_name))

def	export():
	print('## - export - ##')
	global ipa_file_name
	ipa_file_name = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
	ipa_file_name = project_name + "_" + ipa_file_name;
	os.system ('xcodebuild -exportArchive -archivePath %s/build/%s.xcarchive -exportPath %s/%s -exportOptionsPlist %s' %(project_path, project_name, export_path, ipa_file_name, option_plist_path))
	global export_abs_path
	export_abs_path = os.path.expanduser(export_path) # 转绝对路径
	print("ipa文件路径：%s%s/%s.ipa" % (export_abs_path, ipa_file_name, project_name))

def upload_ipa():
	print('## - upload - ##')
	if os.path.exists("%s/%s" % (export_abs_path, ipa_file_name)):
		file_Path = "%s/%s/%s.ipa" % (export_abs_path, ipa_file_name, project_name)
		print('上传中...')
		# 注意，这里需要自行修改，因为服务器后台可能还需要一些参数的验证，也可以上传到第三方平台，根据第三方的要求去-F填写参数，然后进行上传。
		# 蒲公英：curl -F "file=@%s" -F "uKey=你的userKey" -F "_api_key=你的appKey" -F "installType=安装方式" -F "password=密码" -F "updateDescription=更新描述" http://www.pgyer.com/apiv1/app/upload
		os.system('curl -F "upload=@%s" %s' % (file_Path, server_address))

	else:
		print("没有找到ipa文件")

def run():
	# 清理
	clean()
	# 编译
	build_archive()
	# 导出ipa
	export()
	# 上传到服务器
	if server_address:
		upload_ipa()

# - 开始执行 -
run()




