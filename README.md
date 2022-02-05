# 通过pymavlink读取Pixhawk数据  
  
在python编译器中安装pymavlink库后，根据参数表中加粗的参数名称，修改代码中master.recv_match函数的type
参数，即可获得想要的参数（不设定type时获取全部参数）