__CreateJSPath = function (js) {
    var scripts = document.getElementsByTagName("script");
    var path = "";
    for (var i = 0, l = scripts.length; i < l; i++) {
        var src = scripts[i].src;
        if (src.indexOf(js) != -1) {
            var ss = src.split(js);
            path = ss[0];
            break;
        }
    }
    var href = location.href;
    href = href.split("#")[0];
    href = href.split("?")[0];
    var ss = href.split("/");
    ss.length = ss.length - 1;
    href = ss.join("/");
    if (path.indexOf("https:") == -1 && path.indexOf("http:") == -1 && path.indexOf("file:") == -1 && path.indexOf("\/") != 0) {
        path = href + "/" + path;
    }
    return path;
}

//bootPath
var bootPATH = __CreateJSPath("nui.js");

//debugger,此变量用来区别ajax请求是否弹出alert来提示交互错误
mini_debugger = true;   

window['nui_model']=window['nui_model']||'min';


//miniui
document.write('<script src="' + bootPATH + 'jquery/jquery-1.6.2.min.js" type="text/javascript"></sc' + 'ript>');
//document.write('<script src="' + bootPATH + 'jquery-1.8.1.min.js" type="text/javascript"></sc' + 'ript>');
//document.write('<script src="' + bootPATH + 'jquery-1.9.js" type="text/javascript"></sc' + 'ript>');

//默认加载min
if(nui_model=='debug'){
	document.write('<script src="' + bootPATH + 'nui-debug.js" type="text/javascript" ></sc' + 'ript>');
}else if(nui_model=='source'){
	document.write('<script src="' + bootPATH + 'nui-source.js" type="text/javascript" ></sc' + 'ript>');
	document.write('<script src="' + bootPATH + 'source/ext/nui-ext.js" type="text/javascript" ></sc' + 'ript>');
}else{
	document.write('<script src="' + bootPATH + 'nui-min.js" type="text/javascript" ></sc' + 'ript>');
	//document.write('<script src="' + bootPATH + 'source/ext/nui-ext.js" type="text/javascript" ></sc' + 'ript>');
}
document.write('<link href="' + bootPATH + 'themes/default/miniui.css" rel="stylesheet" type="text/css" />');
document.write('<link href="' + bootPATH + 'themes/default/nui-ext.css" rel="stylesheet" type="text/css" />');
document.write('<link href="' + bootPATH + 'themes/icons.css" rel="stylesheet" type="text/css" />');

//mode
//mode
var mode = getCookie("miniuiMode");
if (mode) {
    document.write('<link href="' + bootPATH + '/themes/default/' + mode + '-mode.css" rel="stylesheet" type="text/css" />');
}

//skin
var skin = getCookie("miniuiSkin");
if (skin) {
    document.write('<link href="' + bootPATH + '/themes/' + skin + '/skin.css" rel="stylesheet" type="text/css" />');
}



////////////////////////////////////////////////////////////////////////////////////////
function getCookie(sName) {
    var aCookie = document.cookie.split("; ");
    var lastMatch = null;
    for (var i = 0; i < aCookie.length; i++) {
        var aCrumb = aCookie[i].split("=");
        if (sName == aCrumb[0]) {
            lastMatch = aCrumb;
        }
    }
    if (lastMatch) {
        var v = lastMatch[1];
        if (v === undefined) return v;
        return unescape(v);
    }
    return null;
}

//window['nui']=window['mini'];

