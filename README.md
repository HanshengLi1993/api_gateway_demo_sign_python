<<<<<<< HEAD
#              **阿里云 API Gateway 签名**

##  项目背景

本项目是将阿里云的api签名计算的详细 demo（JAVA）改写成Python。

参照的项目：<https://github.com/aliyun/api-gateway-demo-sign-java>

请求签名说明文档：https://help.aliyun.com/document_detail/29475.html?spm=a2c4e.11153940.blogcont72345.12.31f56773YLuyzE

在本项目中，将学习阿里云API签名设计思路，以及参考java的封装模块思路实现python代码的模块封装。



## 设计思路

API签名是解决了请求的身份是否合法，请求参数是否被篡改，请求是否唯一这三个接口安全问题。

### 请求身份

为开发者分配**AccessKey**（开发者标识，确保唯一）和**SecretKey**（用于接口加密，确保不易被穷举，生成算法不易被猜测）。

在对接口进行签名传计算时，将**AccessKey**放入请求串中能标识请求的身份，同时使用**SecretKey**作为加密的密匙防止了密匙被截获，盗用。

通过校验**AccessKey**对应的**SecretKey**对请求进行签名是否同请求中的签名字段一致，来判断请求的身份是否合法。

###  防止篡改

API需要用户，使用密钥对排序后的请求全部内容（包括请求的Method、HEADERS、URL、QueryString、BODY）计算签名串，并将签名串放入请求，供验证请求身份。

将请求进行HMACSHA256加密，得到的签名是无法被破解的不可逆加密，只用通过对签名串的再次加密，比对两次加密结果才能看出请求是否被篡改。同时签名针对的是所有的请求内容，所以即使请求被拦截，由于不知道**SecretKey**，修改任何值都对无法对签名字段进行修改，导致签名校验失败，因此请求无法被篡改。

### 放重发攻击

重放攻击：攻击者发送一个目的主机已接收过的包，特别是在认证的过程中，用于认证用户身份所接收的包，来达到欺骗系统的目的，主要用于身份认证过程，破坏认证的安全性。这种攻击会不断恶意或欺诈性地重复一个有效的数据传输，重放攻击可以由发起者拦截并重复发该数据到目的主机进行。

#### timestamp+nonce方案

- Timestamp：API 调用者传递时间戳，值为当前时间的毫秒数，也就是从1970年1月1日起至今的时间转换为毫秒，时间戳有效时间为15分钟。
- Nonce：API 调用者生成的 UUID。

假设允许客户端和服务端最多能存在15分钟的时间差，同时追踪记录在服务端的nonce集合。当有新的请求进入时，首先检查携带的timestamp是否在15分钟内，如超出时间范围，则拒绝，然后查询携带的nonce，如存在已有集合，则拒绝。否则，记录该nonce，并删除集合内时间戳大于15分钟的nonce（可以使用redis的expire，新增nonce的同时设置它的超时失效时间为15分钟）。










=======
>>>>>>> fa1367f90fa29e13a1f17699299456fc7bde2a85

