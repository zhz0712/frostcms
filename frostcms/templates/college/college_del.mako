<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>ccms</title>
    <link href="../../static/css/bootstrap.css" rel="stylesheet" media="screen"/>
    <link href="../../static/css/ccms.css" rel="stylesheet" media="screen"/>
    <script src="../../static/js/bootstrap.js"></script>
    <script src="../../static/js/jquery.js"></script>
    <script src="../../static/js/ccms.js"></script>
</head>

<body>
	<!-- 登录模块 -->
    <%include file="/login/login.mako" />
	<!-- 顶部固定栏 -->
    <!--<%include file="/main/head.mako" />-->
	<!-- 导航栏部分 -->
    <%include file="/main/nav_admin.mako" />
    <!-- 主体部分 -->
	<div class="right">
    	
        <!-- 主体头部 -->
		<div class="right_head">
			<div class="title_2">学院管理</div>
			<a class="btn btn-primary" id="btn_head" href="/college/list">返回实验室列表</a>   
		</div>
        
        <!-- 主体信息表 -->
        <div class="right_main">
        	<form action="/college/del" class="add">
 				%if college:
 				<div class="app_name">
        		学院删除
        		</div>
 				<input type="hidden" name="college.id" value="${college.id}"/>
 				<div class="input-prepend">
  					<span class="add-on">名称</span>
  					<input class="span2" id="prependedInput" readOnly="true" type="text" placeholder="" name="college.name" value="${college.name}"/>
				</div>
				<br />
 				<button class="btn btn-danger" id="add_submit" type="submit">确认删除</button>
 				
 				%endif
 			</form>
        </div>               
        
    </div>
</body>
</html>