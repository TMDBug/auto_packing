## 需要配置如下信息
### 一、配置auto_packing.py

填项目路径(末尾不带/)
project_path = "~/Desktop/DENFramework"

填项目名称
project_name = "DENFramework"

填 xcworkspace 或 xcodeproj
project_suffix = "xcworkspace"

填 Release 或 Debug
config = "Release"

如果没有建其他target 和项目名一样
target_name = "DENFramework"

导出路径
export_path  = "~/Desktop"

填exportPlist.plist的路径(末尾不带/)
option_plist_path = "~/Desktop/auto_packing"

上传服务器地址(不填则不上传只导出，上传还需要在代码中自行配置)
server_address = ""

##### 注：代码比较简单，也可以自行修改。
详细说明：[https://www.tmdbug.com/webdev/python/687.html](https://www.tmdbug.com/webdev/python/687.html)
 如有疑问可以 [issue提问](https://github.com/TMDBug/read_ipa_plist/issues)，或者去[TMDBug.com](https://tmdbug.com)留言。

### 二、配置exportOptions.plist

打开后配置下需要填写的就行了。
或者可以事先用手动打包，在导出的ipa文件夹里有个ExportOptions.plist，把里面的信息替换到代码中的exportOption.plist里。
或者直接用导出的ExportOptions.plist替换exportOption.plist。



