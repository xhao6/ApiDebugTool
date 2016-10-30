# ApiDebugTool
露脸云SDK在线debug工具，Python+Flask开发 

已部署于AWS平台，访问地址http://xhao.me/test

本项目分为两部分：

第一部分为RESTful API的“微服务”，负责与SDK coreserver的交互，包括获取token、sessionID、建立账号等操作，以web service的形式供其他应用调用，API文档可见http://xhao.me/test/opendoc；

第二部分是调用第一部分微服务的一个典型方式，由flask-wtforms建立的前端表格页面，用于用户的互动，获取用户的请求然后转发给后端网络服务，将得到的response返回给用户。

由于将本项目解耦成了微服务+前端页面的架构形式，我们可以很方便的在不同场合调用该微服务来快速实现部署，例如建立一个IOS的app，通过HTTP指令来调用微服务，即可快速构建IOS端的API调试工具。
